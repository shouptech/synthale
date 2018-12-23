"""Test interactions with the CLI."""

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
