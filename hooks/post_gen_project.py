import shutil
import subprocess
from pathlib import Path

DEV_DEPS = [
    "black",
    "flake8",
    "flake8-commas",
    "flake8-docstrings",
    "isort",
    "mypy",
    "nox",
    "pytest",
]
subprocess.run(
    ["poetry", "add", "-n", "--dev"] + DEV_DEPS,
    check=True,
)


if "{{ cookiecutter.template }}" == "bin":
    subprocess.run(
        ["poetry", "add", "-n", "click"],
        check=True,
    )
else:
    Path("src/{{ cookiecutter.lib_name }}/__main__.py").unlink()


venv_path = subprocess.run(
    ["poetry", "env", "info", "-p"],
    stdout=subprocess.PIPE,
    check=True,
    text=True,
).stdout.rstrip()
shutil.rmtree(venv_path)
