include .env

.PHONY: help
help: ## Command help.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: clean ## Runs tests.
	# roda unit test and integratoin-test
	docker compose run --rm web sh -c "python ./src/manage.py test src --noinput"

.PHONY: coverage
coverage: lint ## Runs pytest witj coverage parameters.
	pytest --cov-config=setup.cfg --cov=. tests/ --cov-report=html --cov-report=xml

.PHONY: up
up: ## Start the localstack (fake cloud local environment).
	@docker compose up -d

.PHONY: down
down: ## Stop and remove the docker container image.
	@docker compose down

.PHONY: migrate
migrate: ## Run django migrate.
	@echo "Migrating..."
	docker compose run --build --rm web sh -c "python ./src/manage.py makemigrations && python ./src/manage.py migrate"

.PHONY: makemigrations
makemigrations: ## Run django makemigrations.
	@echo "Makemigrations..."
	docker compose run --build --rm web sh -c "python ./src/manage.py makemigrations"

.PHONY: psql
psql: ## Access the postgres command line interface.
	@docker exec -ti db bash -c "psql -h localhost -U $(POSTGRES_USER) -d $(POSTGRES_DB)"