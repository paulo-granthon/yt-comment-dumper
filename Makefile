.PHONY: all \
	prep prepare \
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

etl:
	@poetry run python src/etl/main.py $(VIDEO)
