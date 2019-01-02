"""Contains the commands for the CLI interface."""

# Copyright (C) 2019 Mike Shoup
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import platform

import click

from synthale import VERSION
from synthale.recipes import load_file, load_all_files, write_recipes


@click.group()
def cli():
    """Synthale converts BeerXML files to markdown."""
    pass


@cli.command()
def version():
    """Print version and exit."""
    click.echo(
        'Synthale version: {}\n'
        'Python version: {}'.format(VERSION, platform.python_version())
    )


@cli.command()
@click.option(
    '--vol-unit', '-v',
    type=click.Choice(('gallons', 'liters')),
    default='gallons',
    help='Unit to display volumes in. Default is gallons.'
)
@click.option(
    '--hop-unit', '-H',
    type=click.Choice(('ounces', 'pounds', 'grams', 'kilograms')),
    default='ounces',
    help='Unit to display hop masses in. Default is ounces.'
)
@click.option(
    '--fermentable-unit', '-f',
    type=click.Choice(('ounces', 'pounds', 'grams', 'kilograms')),
    default='pounds',
    help='Unit to display fermentable masses in. Default is pounds.'
)
@click.option(
    '--temp-unit', '-f',
    type=click.Choice(('celsius', 'fahrenheit')),
    default='fahrenheit',
    help='Unit to display temperatures in. Default is fahrenheit.'
)
@click.argument('input_path')
@click.argument('output_path')
def generate(
    input_path,
    output_path,
    vol_unit,
    hop_unit,
    fermentable_unit,
    temp_unit
):
    """Generate markdown files from BeerXML files.

    INPUT_PATH is either a directory containing XML files, or an individual XML
    file. OUTPUT_PATH is the directory to write the markdown files to.
    """
    units = {
        'vol_unit': vol_unit,
        'hop_unit': hop_unit,
        'fermentable_unit': fermentable_unit,
        'temp_unit': temp_unit
    }

    click.echo("Generating markdown from '{}'...".format(input_path))

    if input_path.endswith('.xml'):
        recipes = load_file(input_path, units)
    else:
        recipes = load_all_files(input_path, units)

    write_recipes(recipes, output_path)
