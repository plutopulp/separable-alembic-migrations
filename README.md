This is a basic example showing how to set up multiple python API services connecting to a single database.
API layers are implemented using FastAPI and the DB layer uses sqlalchemy and alembic.
Migrations are managed independently in each API service.

We implement this by creating a database schema for each application and then tying all tables of an application to the respective schema. We create an alembic declarative_base model, `Base`, for each schema and ensure that autogenerated alembic version revisions for a given `Base` only target DB objects under that same schema.

# Starting the services

To spin up all the service, run

```shell
make start-db
```

This will start up a PostgreSQL database, an adminer client for managing the DB content, and 2 fastapi applications, `billing` and `auth`.

The DB client should then be available on your [localhost:8080](http://localhost:8080).
Login as user, `postgres`, password, `postgres` and database, `test_db`.
The Auth API reference is available at [localhost:5008](http://localhost:5008).
The billing API reference is available at [localhost:5009](http://localhost:5009).

On initialisation, a `init.sql` script gets triggered which creates the DB schemas that each table set gets attached to.
You should be able to see these schemas in the dropdown menu in [adminer](http://localhost:8080/?pgsql=db&username=postgres&db=test_db&ns=public), alongside the default schemas, such as `public`, `pg_catalogue`, etc...
When each API service is started, the DB is migrated to the `alembic` head version.
You should be able to see different table sets, for `auth` and `billing`, under their respective schemas.
Notice that an `alembic_version` table exists under each schema, which is responsible for recording all the versions of the tables under that schema.

# Migrations

## Migrating to head version

Although the DB should have been migrated to the `HEAD` on startup, you can upgrade the database migrations of either schema to the head version of, by running

```shell
make migrate svc=TARGET_SERVICE
```

where `TARGET_SVC` is one of the target service names in the docker-compose.yml, i.e `billing`, `auth`.

## Auto-generating revisions

To perform auto-generated revisions for a given schema, update your `models.py` in one of the services and then run:

```shell
make add-migration svc=TARGET_SVC msg="YOUR_VERSION_MESSAGE"
```

You should see a new auto-generated migration file under `alembic/versions`, which should reflect the changes you have made to your models. No DB objects from other schemas should be referenced in this file.

To apply the migrations to the DB, upgrade your version to point to the head:

```shell
make migrate svc=TARGET_SVC
```

# Implementation details

## Schema definitions

For each application, we create a PostgreSQL schema. In the example, this is achieved by bind mounting an `init.sql` file, e.g.

```SQL
CREATE SCHEMA IF NOT EXISTS auth AUTHORIZATION postgres;
CREATE SCHEMA IF NOT EXISTS billing AUTHORIZATION postgres;
```

to the postgres docker-compose service.

We ensure that any tables for a given app are attached to their respective schema, by configuration the metadata of the `Base` model:

```python
from sqlalchemy import MetaData
from sqlalchemy.orm import registry

mapper_registry = registry()
_Base = mapper_registry.generate_base()

class Base(_Base):
    ...
    metadata = MetaData(schema=os.environ["DB_SCHEMA"])
    ...
```

where the `DB_SCHEMA` is defined in each apps' environment.

## Migration configuration

We want the various applications to be able to migrate their respective DB objects (attached to their schema), independently from each other.
We also want to leverage the autogenerate feature of `alembic` to automatically generate the content of migration version files.
`alembic` achieves this by inspecting the difference in the current state of the DB and the current model definitions inheriting from the `Base` model.
That means that by default, if we were to perform a revision attached to a `Base` for a particular app, all the tables associated with the other apps (other schemas) would be dropped.
This is because the state of the DB will actually include these tables, but the tables won't exist under the target `Base`.
Hence we need a way to configure the migrations such that only objects tied to a particular schema are considered as candidates to migrate.

To achieve this we define the following configuration:

```python
MIGRATIONS_CONFIG = dict(
    target_metadata=target_metadata,
    version_table="alembic_version",
    version_table_schema=DB_SCHEMA,
    include_schemas=True,
    include_name=include_name,
)
```

where `DB_SCHEMA = os.environ["DB_SCHEMA"]` and the callback function:

```python
def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name in [DB_SCHEMA]
    return True
```

which will ensure only objects under the target schema are included.
Note also that we have defined `version_table_schema=DB_SCHEMA` such that the actual `alembic_version` table responsible for tracking migrations lives on the `DB_SCHEMA` too.
