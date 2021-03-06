.PHONY: install quality style test

check_dirs := setup.py tests

clean:
	rm -rf docs/build

docs: clean
ifeq ($(origin smv), undefined)
	sphinx-build -M html docs/source docs/build
else
	sphinx-multiversion docs/source docs/build
endif

gh-pages:
	.ci/gh-pages.sh

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
