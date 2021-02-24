import nox  # type: ignore


nox.options.default_venv_backend = "none"


@nox.session
def install(session):
    session.run_always("poetry", "install")


@nox.session
def black(session):
    session.run("poetry", "run", "black", "--check", ".")


@nox.session
def isort(session):
    session.run("poetry", "run", "isort", "--check", ".")


@nox.session
def flake8(session):
    session.run("poetry", "run", "flake8")


@nox.session
def mypy(session):
    session.run("poetry", "run", "mypy", ".")


@nox.session
def pytest(session):
    session.run("poetry", "run", "pytest")


@nox.session
def safety(session):
    session.run("poetry", "run", "safety", "check")
