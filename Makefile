.PHONY: install quality style test

check_dirs := setup.py tests

install:
	pip install -e ".[dev]"

quality:
	black --check $(check_dirs)
	isort --check-only $(check_dirs)
	flake8 $(check_dirs)

style:
	black $(check_dirs)
	isort $(check_dirs)

test:
	pytest -v
