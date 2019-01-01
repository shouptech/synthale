"""Test interactions with the CLI."""

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

from click.testing import CliRunner

from synthale.cli import main


def test_main_help():
    """Test the help output of the main CLI command."""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert 'INPUT_PATH' in result.output
    assert 'OUTPUT_PATH' in result.output


def test_main_directory(tmpdir, md_recipes):
    """Test command where input is a directory."""
    runner = CliRunner()
    result = runner.invoke(main, ['tests/recipes', str(tmpdir)])

    assert result.exit_code == 0
    assert result.output.startswith(
        "Generating markdown from 'tests/recipes'..."
    )

    for recipe in md_recipes:
        path = tmpdir.join(recipe.filename)
        assert path.read() == recipe.markdown


def test_main_file(tmpdir):
    """Test command where input is a file."""
    runner = CliRunner()
    result = runner.invoke(main, ['tests/recipes/weizen.xml', str(tmpdir)])

    assert result.exit_code == 0
    assert result.output.startswith(
        "Generating markdown from 'tests/recipes/weizen.xml'..."
    )

    path = tmpdir.join('weizen.md')
    assert path.read().startswith('Weizen')
