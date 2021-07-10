{{ '*'  * cookiecutter.repo_name | length }}
{{ cookiecutter.repo_name }}
{{ '*'  * cookiecutter.repo_name | length }}

Custom Sphinx theme baed on the ubiquitous `Read the Docs
<https://github.com/readthedocs/sphinx_rtd_theme>`_ theme. It overrides the Read the
Docs theme with custom components and styles.

Installation
============

Install the theme by adding the following to your library's ``setup.py``:

.. code:: python

    from setuptools import setup


    extras = {
        ...
        "docs": [
            "{{ cookiecutter.import_name }} @ {{ cookiecuter.repo_url }}",
        ],
    }

    setup(
        ...
        extras_require=extras,
    )

In your Sphinx ``conf.py``, make sure to include the following:

.. code:: python

    extensions = [
        ...
        "{{ cookiecutter.import_name }}",
    ]

    html_theme = "{{ cookiecutter.import_name }}"

Either build the documentation from your current branch using a tradition Sphinx build
script, or build a versioned site using the following:

.. code:: bash

    sphinx-multiversion docs/source docs/build

.. toctree::
    :caption: Demo Documentation
    :hidden:

    demo/structure
    demo/demo
    demo/list_tables
    demo/api
