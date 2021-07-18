#!/bin/bash

set -eo pipefail

git config --global url."https://${GITHUB_TOKEN}@github".insteadOf "https://github"

git config --local user.name "{{ cookiecutter.author_name }}"
git config --local user.email "{{ cookiecutter.author_email }}"
