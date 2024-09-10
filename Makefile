run:
	poetry run python src/main.py

lint:
	poetry run ruff check

lintfix: format
	poetry run ruff check --fix

format:
	poetry run ruff format

test:
	pytest