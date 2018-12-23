"""Contains the commands for the CLI interface."""

import click


@click.command()
@click.argument('input')
@click.argument('output')
def main(input, output):
    """Generate markdown files from BeerXML files.

    INPUT is either a directory containing XML files, or an individual XML
    file. OUTPUT is the directory to write the markdown files to.
    """
    pass
