"""Contains the commands for the CLI interface."""

import click


@click.group()
def cli():
    """Synthale generates Markdown files from BeerXML files."""
    pass
