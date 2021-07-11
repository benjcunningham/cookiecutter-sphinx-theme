import datetime
import os
import sys


sys.path.insert(0, os.path.abspath("../../src"))
sys.path.append(os.path.abspath("./demo/"))

project = "{{ cookiecutter.repo_name }}"
copyright = "{}, {}.".format(datetime.datetime.now().year, {{ cookiecutter.author_name }})
author = "{{ cookiecutter.author_name }}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_multiversion",
    "{{ cookiecutter.import_name }}",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "{{ cookiecutter.import_name }}"

smv_branch_whitelist = r"^(master|develop|release\/.*)$"
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"
smv_released_pattern = r"^.*(tags|master).*$"
smv_remote_whitelist = r"^(origin)$"
