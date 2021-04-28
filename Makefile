black:
	black pandas_database_profiler
	black tests

black-diff:
	black pandas_database_profiler --diff
	black tests --diff

build:
	docker build -f Dockerfile --tag pandas-database-profiler:latest .

export:
	poetry export -f requirements.txt -o requirements.txt
	poetry export -f requirements.txt -o requirements_dev.txt --dev

flake8:
	flake8 pandas_database_profiler/ tests/ --statistics

install:
	poetry install

pre-commit: black flake8 test build

run-container: build
	docker container run -p 8501:8501 -d pandas-database-profiler:latest

run-server:
	streamlit run pandas_database_profiler/main.py

test:
	pytest -vvs --cov-report term-missing --cov=pandas_database_profiler tests/

_update:
	poetry update

update: _update export pre-commit

update-diff:
	poetry update --dry-run | grep -i updat
