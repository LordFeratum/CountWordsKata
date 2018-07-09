.PHONY: test


all: build run

build:
	docker-compose build

run:
	docker-compose run --rm word-count run ${args}

build-test:
	docker-compose -f docker-compose.yaml -f docker-compose.test.yaml build

test:
	docker-compose -f docker-compose.yaml -f docker-compose.test.yaml up
