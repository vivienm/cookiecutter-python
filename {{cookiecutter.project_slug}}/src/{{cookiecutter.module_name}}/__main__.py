import click

from . import __version__


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli() -> None:
    """{{ cookiecutter.description }}"""
    print("Hello world!")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
