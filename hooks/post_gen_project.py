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
            ["poetry", "add", "--lock", "--no-interaction", *args],
            check=True,
        )


def install_dev_dependencies() -> None:
    poetry_add(["--dev", *DEV_DEPS])


def install_lib_dependencies() -> None:
    poetry_add(LIB_DEPS)


def install_bin_dependencies() -> None:
    poetry_add(BIN_DEPS)


def remove_main() -> None:
    Path("src/{{ cookiecutter.module_name }}/__main__.py").unlink()


def remove_poetry_venv() -> None:
    venv_path = subprocess.run(
        ["poetry", "env", "info", "-p"],
        stdout=subprocess.PIPE,
        check=True,
        text=True,
    ).stdout.rstrip()
    shutil.rmtree(venv_path)


def setup_vcs() -> None:
    if "{{ cookiecutter.version_control }}" == "git":
        subprocess.run(["git", "init"], check=True)
    else:
        Path(".gitignore").unlink()


def setup_ci() -> None:
    if "{{ cookiecutter.continuous_integration }}" != "github":
        gh_path = Path(".github")
        shutil.rmtree(gh_path / "workflows")
        if next(gh_path.iterdir(), None) is None:
            gh_path.rmdir()
    if "{{ cookiecutter.continuous_integration }}" != "gitlab":
        Path(".gitlab-ci.yml").unlink()


def main() -> None:
    install_lib_dependencies()
    if "{{ cookiecutter.project_kind }}" == "bin":
        install_bin_dependencies()
    else:
        remove_main()
    install_dev_dependencies()
    remove_poetry_venv()
    setup_vcs()
    setup_ci()


if __name__ == "__main__":
    main()
