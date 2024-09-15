PROJECT_NAME = "urban-octo-engine"

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
	pytest -vvl $(TEST_ARGS)

lint: black pyright isort flake8 djlint

black:
	black . --config pyproject.toml

pyright:
	pyright .

isort:
	isort .

flake8:
	pflake8 .

djlint:
	djlint . --extension=html --reformat

prep_migration:
	python payment/manage.py makemigrations payments
	@echo "Now run: python payment/manage.py sqlmigrate payments XXXX"

migrate:
	python payment/manage.py migrate

collectstatic:
	python payment/manage.py collectstatic --noinput

run:
	cd payment && gunicorn main.wsgi --bind "$(HOST):$(PORT)" --workers 7 --timeout 800

clear:
	find . -name \*.pyc -delete
