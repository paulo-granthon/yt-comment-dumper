.PHONY: all \
	prep prepare \
	serve server \
	etl \
	db-up \
	db-down

%:
	@:

all: prep etl

prep: prepare
prepare:
	@poetry lock
	@poetry install

serve: server
server:
	@poetry run python src/server/app.py

etl:
	@poetry run python src/etl/main.py $(VIDEO)
