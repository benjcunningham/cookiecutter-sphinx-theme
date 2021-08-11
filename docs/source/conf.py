import datetime
import os
import sys


project = "cookiecutter-sphinx-theme"
copyright = "{}, {}.".format(datetime.datetime.now().year, "Ben Cunningham")
author = "Ben Cunningham"

extensions = [
    "sphinx_multiversion",
    "sphinx_benjcunningham_theme",
]

html_theme = "sphinx_benjcunningham_theme"

smv_branch_whitelist = r"^(master|develop|release\/.*)$"
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"
smv_released_pattern = r"^.*(tags|master).*$"
smv_remote_whitelist = r"^(origin)$"
