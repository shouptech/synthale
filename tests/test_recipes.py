"""Contains tests for the synthale.recipes module."""

import pybeerxml

from synthale.recipes import (
    MarkdownRecipe, load_file, load_all_files, write_recipes
)


def test_load_file(capsys):
    """Load the sample XML file and ensure the name is parsed."""
    result = load_file('tests/recipes/weizen.xml')
    assert result[0].recipe.name == 'Weizen'

    result = load_file('tests/recipes/bad-file')
    captured = capsys.readouterr()
    assert result == []
    assert captured.err == ('Error parsing tests/recipes/bad-file: '
                            'syntax error: line 1, column 0\n')


def test_load_all_files():
    """Load all sample XML files and ensure the count is correct."""
    result = load_all_files('tests/recipes')
    result.sort(key=lambda item: item.recipe.name)
    assert len(result) == 2
    assert result[0].recipe.name == 'Coffee Stout'
    assert result[1].recipe.name == 'Weizen'


def test_markdown_recipe_filename():
    """Validate a generated markdown recipe's filename."""
    xml_recipe = pybeerxml.Recipe()
    xml_recipe.name = 'Validate@!#This!'
    recipe = MarkdownRecipe(xml_recipe)
    assert recipe.filename == 'validate_this.md'


def test_markdown_recipe_name():
    """Validate generated name for recipe."""
    xml_recipe = pybeerxml.Recipe()
    xml_recipe.name = 'Foobar'
    recipe = MarkdownRecipe(xml_recipe)
    assert recipe.name == 'Foobar\n======'


def test_markdown_recipe_style():
    """Validate generated style for recipe."""
    xml_recipe = pybeerxml.Recipe()
    xml_recipe.style = pybeerxml.style.Style()
    xml_recipe.style.style_guide = 'BJCP'
    xml_recipe.style.style_letter = 'E'
    xml_recipe.style.category_number = 13
    xml_recipe.style.name = 'American Stout'
    recipe = MarkdownRecipe(xml_recipe)
    assert recipe.style == (
        'Style\n'
        '-----\n'
        '**Style guide**: BJCP\n'
        '**Style category**: 13E\n'
        '**Style name**: American Stout'
    )


def test_recipe_details(md_weizen):
    """Test valid details are generated."""
    md_weizen.vol_unit = 'gallons'
    assert md_weizen.details == (
        'Details\n'
        '-------\n'
        '**Type**: All Grain\n'
        '**Batch efficiency**: 72.0 %\n'
        '**Boil size**: 6.3 gal\n'
        '**Boil length**: 60 min\n'
        '**Batch size**: 5.5 gal\n'
        '**Estimated OG**: 1.051\n'
        '**Estimated FG**: 1.015\n'
        '**Estimated IBU**: 15\n'
        '**Estimated SRM**: not implemented\n'
        '**Estimated ABV**: 4.7'
    )

    md_weizen.vol_unit = 'liters'
    assert '**Boil size**: 23.7 L' in md_weizen.details
    assert '**Batch size**: 20.8 L' in md_weizen.details


def test_write_recipes(md_recipes, tmpdir):
    """Test write_recipes function."""
    write_recipes(md_recipes, str(tmpdir))

    for recipe in md_recipes:
        path = tmpdir.join(recipe.filename)
        assert path.read() == recipe.markdown
