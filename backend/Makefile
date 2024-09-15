PROJECT_NAME = "urban-octo-engine"
PROJECT_DIR = app

HOST ?= 127.0.0.1
PORT ?= 8000

.PHONY: deploy

pyenv:
	echo $(PROJECT_NAME) > .python-version && pyenv install -s 3.11.4 && pyenv virtualenv -f 3.11.4 $(PROJECT_NAME)

pyenv-delete:
	pyenv virtualenv-delete -f $(PROJECT_NAME)

install-dev-deps: dev-deps
	pip-sync requirements.txt dev-requirements.txt

install-deps: deps
	pip-sync requirements.txt

deps:
	pip install --upgrade pip pip-tools
	pip-compile --output-file requirements.txt --resolver=backtracking pyproject.toml

dev-deps: deps
	pip-compile --extra=dev --output-file dev-requirements.txt --resolver=backtracking pyproject.toml

check: lint test

test:
	@cd ${PROJECT_DIR} && python manage.py test

lint: black pyright isort flake8 djlint

black:
	black . --config pyproject.toml

pyright:
	pyright .

isort:
	isort .

flake8:
	flake8 .

djlint:
	djlint . --extension=html --reformat

prep_migration:
	python ${PROJECT_DIR}/manage.py makemigrations ${PROJECT_NAME}
	@echo "Now run: python ${PROJECT_DIR}/manage.py sqlmigrate ${PROJECT_NAME} XXXX"

migrate:
	python ${PROJECT_DIR}/manage.py migrate

collectstatic:
	python ${PROJECT_DIR}/manage.py collectstatic --noinput

run:
	cd ${PROJECT_DIR} && gunicorn --bind ${HOST}:${PORT} main.wsgi:application --workers 7 --timeout 800

clear:
	find . -name \*.pyc -delete
