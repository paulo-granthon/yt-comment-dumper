.PHONY: all \
	prep prepare \
	serve server \
	etl \
	db-up \
	db-down

%:
	@:

all: prep db-up etl serve db-down

prep: prepare
prepare:
	@poetry lock
	@poetry install

db-up:
	@docker-compose up -d

db-down:
	@docker-compose down

serve: server
server:
	@poetry run python src/server/app.py

etl:
	@poetry run python src/etl/main.py $(VIDEO)
