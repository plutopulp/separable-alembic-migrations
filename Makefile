.PHONY: build start down teardown

# Project name for the containers
PROJECT_NAME := separable-migrations


build:
	docker-compose --project-name $(PROJECT_NAME) build

start: build
	docker-compose --project-name $(PROJECT_NAME) up

stop:
	docker-compose  --project-name $(PROJECT_NAME) down

teardown:
	docker-compose --project-name $(PROJECT_NAME) down --volumes --remove-orphans

upgrade-head-a: 
	docker-compose --project-name $(PROJECT_NAME) run --rm app_a poetry run alembic upgrade head

add-migration-a: upgrade-head-a
	docker-compose --project-name $(PROJECT_NAME) run --rm app_a poetry run alembic revision --autogenerate -m "$(m)"

undo-migration-a: upgrade-head-a
	docker-compose --project-name $(PROJECT_NAME) run --rm app_a poetry run alembic downgrade "$(n)"

upgrade-head-b: 
	docker-compose --project-name $(PROJECT_NAME) run --rm app_b poetry run alembic upgrade head

add-migration-b: upgrade-head-b
	docker-compose --project-name $(PROJECT_NAME) run --rm app_b poetry run alembic revision --autogenerate -m "$(m)"

undo-migration-b: upgrade-head-b
	docker-compose --project-name $(PROJECT_NAME) run --rm app_b poetry run alembic downgrade "$(n)"