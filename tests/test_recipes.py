"""Contains tests for the synthale.recipes module."""

from synthale.recipes import parse_xmlfile, load_recipes, name_to_slug


def test_parse_xmlfile():
    """Load the sample XML file and ensure the name is parsed."""
    result = parse_xmlfile('tests/recipes/weizen.xml')
    assert result[0].name == 'Weizen'


def test_load_recipes():
    """Load all sample XML files and ensure the count is correct."""
    result = load_recipes('tests/recipes')
    result.sort(key=lambda recipe: recipe.name)
    assert len(result) == 2
    assert result[0].name == 'Coffee Stout'
    assert result[1].name == 'Weizen'


def test_name_to_slug():
    """Ensure names are properly converted to slugs."""
    name = 'Convert!This name@$  @!to a slug.'
    assert name_to_slug(name) == 'convert_this_name_to_a_slug'
