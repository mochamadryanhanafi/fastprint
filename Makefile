.PHONY: build up down logs shell migrate populate clean help

help:
	@echo "Available commands:"
	@echo "  build       Build the docker images"
	@echo "  up          Start the docker containers"
	@echo "  down        Stop the docker containers"
	@echo "  logs        View logs from containers"
	@echo "  shell       Access the web container shell"
	@echo "  migrate     Run database migrations"
	@echo "  populate    Run the populate_products command"
	@echo "  clean       Remove containers and volumes"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec web bash

migrate:
	docker-compose exec web python manage.py migrate

populate:
	docker-compose exec web python manage.py populate_products

check:
	docker-compose exec web python manage.py check

clean:
	docker-compose down -v
