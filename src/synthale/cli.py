"""Contains the commands for the CLI interface."""

# Copyright (C) 2019 Mike Shoup
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
