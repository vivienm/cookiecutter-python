# Python project template

An opinionated Cookiecutter template for Python projects.

## Features

* Package management with [Poetry](https://python-poetry.org/), using the [src directory layout](https://hynek.me/articles/testing-packaging/).
* Formatting with [Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/).
* Linting with [Flake8](https://flake8.pycqa.org/en/latest/) and [pydocstyle](https://github.com/PyCQA/pydocstyle/).
* Typechecking with [Mypy](https://mypy.readthedocs.io/).
* Testing with [pytest](https://docs.pytest.org/en/stable/) and [Nox](https://nox.thea.codes/en/stable/).
* Checking vulnerabilities with [Safety](https://pyup.io/safety/).
* Continous integration with [GitHub actions](https://github.com/features/actions) and [GitLab CI](https://docs.gitlab.com/ce/ci/).
* Command line argument parsing with [Click](https://click.palletsprojects.com/).

## Quickstart

Install the latest [Cookiecutter](https://cookiecutter.readthedocs.io/) if you haven't installed it yet.
You can refer to installation instructions [here](https://cookiecutter.readthedocs.io/en/latest/installation.html), or use [pipx](https://pipxproject.github.io/pipx/):

```console
$ pipx install cookiecutter
```

To generate a Python package project, run:

```console
$ cookiecutter . -o ~/projects/
```

## Configuration

* `project_kind`: Choose whether the project provides a command line utility (`bin`) or is a pure library (`lib`).
* `project_name`: Your project fancy name, with capitals, whitespaces and
whatnots.
Used as title in the README file.
* `project_slug`: The lowercase, dash-separated version of the project title.
Used as toplevel directory name.
* `module_name`: Name of the toplevel Python package for this project.
* `script_name`: If the project provides a command line utility (`project_kind = bin`), choose its name.
* `description`: A short sentence to describe the project.
Used in the README file, command line help and package metadata.
* `license`: The project license.
* `author_name` and `author_email`: Name and email address of the author.
* `python_version`: Python version to use in the project (format: `major.minor`).
* `readme_format`: use Markdown (`md`) or reStructuredText (`rst`) format in the project README.
* `version_control`: Whether to initialize a new Git repository for the project.
* `continuous_integration`: Optionaly use GitHub actions or GitLab CI for running tests.
