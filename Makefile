.PHONY: build start down teardown upgrade-head add-migration undo-migration

# Project name for the containers
PROJECT_NAME := separable-migrations

build:
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) build

start: build
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) up

stop:
	docker-compose  -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) down

teardown:
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) down --volumes --remove-orphans

upgrade-head: 
	docker-compose --f ./docker/docker-compose.yml -project-name $(PROJECT_NAME) run --rm "$(app)" poetry run alembic upgrade head

revision: 
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) run --rm "$(app)" poetry run alembic revision --autogenerate -m "$(m)"

downgrade:
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) run --rm "$(app)" poetry run alembic downgrade "$(n)"
