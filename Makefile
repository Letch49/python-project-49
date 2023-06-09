# Bash

up:
	poetry install
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-venv:
	python3 -m pip install --force-reinstall  dist/*.whl

lint:
	poetry run flake8 brain_games