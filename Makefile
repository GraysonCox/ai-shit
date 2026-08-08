.PHONY: test

docker-build:
	docker build -t bot .

docker-run:
	docker run -e DISCORD_TOKEN=${DISCORD_TOKEN} bot

build:
	uv sync

run:
	DISCORD_TOKEN=${DISCORD_TOKEN} uv run python src/main.py

lint-cfn:
	uv run cfn-lint
lint-yaml:
	uv run yamllint .
lint-python:
	uv run ruff check
lint: lint-cfn lint-yaml lint-python
test:
	uv run pytest
verify: lint test

format:
	uv run isort .
	uv run ruff format
