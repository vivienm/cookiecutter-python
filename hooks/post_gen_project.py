import shutil
import subprocess
from pathlib import Path
from typing import Collection


DEV_DEPS = (
    "black",
    "flake8",
    "flake8-commas",
    "flake8-docstrings",
    "isort",
    "mypy",
    "pytest",
)


LIB_DEPS = ()


BIN_DEPS = ("click",)


def poetry_add(args: Collection[str]) -> None:
    if len(args) != 0:
        subprocess.run(
            ["poetry", "add", "-n", *args],
            check=True,
        )


def install_dev_dependencies() -> None:
    poetry_add(["--dev", *DEV_DEPS])


def install_lib_dependencies() -> None:
    poetry_add(LIB_DEPS)


def install_bin_dependencies() -> None:
    poetry_add(BIN_DEPS)


def remove_poetry_venv() -> None:
    venv_path = subprocess.run(
        ["poetry", "env", "info", "-p"],
        stdout=subprocess.PIPE,
        check=True,
        text=True,
    ).stdout.rstrip()
    shutil.rmtree(venv_path)


def main() -> None:
    install_lib_dependencies()
    if "{{ cookiecutter.template }}" == "bin":
        install_bin_dependencies()
    else:
        Path("src/{{ cookiecutter.lib_name }}/__main__.py").unlink()
    install_dev_dependencies()
    remove_poetry_venv()


if __name__ == "__main__":
    main()
