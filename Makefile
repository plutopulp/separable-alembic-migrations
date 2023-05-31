.PHONY: build start down teardown migrate add-migration undo-migration

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

migrate: 
	docker-compose --f ./docker/docker-compose.yml -project-name $(PROJECT_NAME) run --rm "$(svc)" alembic upgrade head

add-migration: 
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) run --rm "$(svc)" alembic revision --autogenerate -m "$(msg)"

downgrade:
	docker-compose -f ./docker/docker-compose.yml --project-name $(PROJECT_NAME) run --rm "$(svc)" alembic downgrade "$(n)"
