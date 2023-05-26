.PHONY: build start down teardown upgrade-head add-migration undo-migration

# Project name for the containers
PROJECT_NAME := separable-migrations

build:
	docker-compose --project-name $(PROJECT_NAME) build

start-db: build
	docker-compose --project-name $(PROJECT_NAME) up db adminer

stop:
	docker-compose  --project-name $(PROJECT_NAME) down

teardown:
	docker-compose --project-name $(PROJECT_NAME) down --volumes --remove-orphans

upgrade-head: 
	docker-compose --project-name $(PROJECT_NAME) run --rm "$(app)" poetry run alembic upgrade head

revision: 
	docker-compose --project-name $(PROJECT_NAME) run --rm "$(app)" poetry run alembic revision --autogenerate -m "$(m)"

downgrade:
	docker-compose --project-name $(PROJECT_NAME) run --rm "$(app)" poetry run alembic downgrade "$(n)"
