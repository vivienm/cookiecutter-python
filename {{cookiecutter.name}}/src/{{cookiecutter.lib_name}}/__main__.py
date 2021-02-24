import click

from . import __version__


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """{{cookiecutter.description}}"""
    print("Hello world!")


def main():
    cli(auto_envvar_prefix="{{cookiecutter.bin_name.replace('-', '_').upper()}}")


if __name__ == "__main__":
    main()
