"""Contains the commands for the CLI interface."""

import click

from synthale.recipes import load_file, load_all_files, write_recipes


@click.command()
@click.argument('input_path')
@click.argument('output_path')
def main(input_path, output_path):
    """Generate markdown files from BeerXML files.

    INPUT_PATH is either a directory containing XML files, or an individual XML
    file. OUTPUT_PATH is the directory to write the markdown files to.
    """
    click.echo("Generating markdown from '{}'...".format(input_path))

    if input_path.endswith('.xml'):
        recipes = load_file(input_path)
    else:
        recipes = load_all_files(input_path)

    write_recipes(recipes, output_path)
