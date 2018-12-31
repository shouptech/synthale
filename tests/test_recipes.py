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
        '**Style guide**: BJCP\\\n'
        '**Style category**: 13E\\\n'
        '**Style name**: American Stout'
    )


def test_recipe_details(md_weizen):
    """Test valid details are generated."""
    md_weizen.vol_unit = 'gallons'
    assert md_weizen.details == (
        'Details\n'
        '-------\n'
        '**Type**: All Grain\\\n'
        '**Batch efficiency**: 72.0 %\\\n'
        '**Boil size**: 6.3 gal\\\n'
        '**Boil length**: 60 min\\\n'
        '**Batch size**: 5.5 gal\\\n'
        '**Estimated OG**: 1.051\\\n'
        '**Estimated FG**: 1.015\\\n'
        '**Estimated IBU**: 15\\\n'
        '**Estimated SRM**: 3.0\\\n'
        '**Estimated ABV**: 4.7 %'
    )

    md_weizen.vol_unit = 'liters'
    assert '**Boil size**: 23.7 L' in md_weizen.details
    assert '**Batch size**: 20.8 L' in md_weizen.details


def test_recipe_fermentables(md_weizen):
    """Test valid fermentable table is generated."""
    md_weizen.fermentable_unit = 'pounds'
    assert md_weizen.fermentables == (
        'Fermentables\n'
        '------------\n'
        '| Name            | Type      | Color  | Amount  |\n'
        '| --------------- | --------- | ------ | ------- |\n'
        '| Pilsner (DE)    | Base Malt | 1.0 °L | 5.00 lb |\n'
        '| Wheat Malt (DE) | Adjunct   | 2.0 °L | 5.00 lb |'
    )

    md_weizen.fermentable_unit = 'ounces'
    assert '| 80.0 oz |' in md_weizen.fermentables

    md_weizen.fermentable_unit = 'grams'
    assert '| 2268.0 g |' in md_weizen.fermentables

    md_weizen.fermentable_unit = 'kilograms'
    assert '| 2.27 kg |' in md_weizen.fermentables


def test_recipe_hops(md_weizen):
    """Test valid hop table is generated."""
    md_weizen.hop_unit = 'ounces'
    assert md_weizen.hops == (
        'Hops\n'
        '----\n'
        '| Name                 | Origin  | Alpha | Amount | Time | Use  |\n'
        '| -------------------- | ------- | ----- | ------ | ---- | ---- |\n'
        '| Northern Brewer (DE) | Germany | 4.9 % | 1.0 oz | 60   | Boil |'

    )

    md_weizen.hop_unit = 'pounds'
    assert '| 0.06 lb |' in md_weizen.hops

    md_weizen.hop_unit = 'kilograms'
    assert '| 0.03 kg |' in md_weizen.hops

    md_weizen.hop_unit = 'grams'
    assert '| 28.3 g |' in md_weizen.hops


def test_recipe_yeast(md_weizen):
    """Test valid yeast table is generated."""
    assert md_weizen.yeast == (
        'Yeast\n'
        '-----\n'
        '| Name          | Lab       | Type | Attenuation |\n'
        '| ------------- | --------- | ---- | ----------- |\n'
        '| Safbrew WB-06 | Fermentis | Ale  | 70.0 %      |'
    )


def test_recipe_miscs(md_coffee_stout, md_weizen):
    """Test valid miscellaneous ingredient table is generated."""
    assert md_coffee_stout.miscs == (
        'Other Ingredients\n'
        '-----------------\n'
        '| Name            | Use | Amount   |\n'
        '| --------------- | --- | -------- |\n'
        '| Coffee (Brewed) | Keg | 24.0 oz. |'
    )

    md_coffee_stout.recipe.miscs[0].display_amount = None
    assert md_coffee_stout.miscs == (
        'Other Ingredients\n'
        '-----------------\n'
        '| Name            | Use | Amount |\n'
        '| --------------- | --- | ------ |\n'
        '| Coffee (Brewed) | Keg | 0.71 L |'
    )

    md_coffee_stout.recipe.miscs[0].amount_is_weight = True
    assert md_coffee_stout.miscs == (
        'Other Ingredients\n'
        '-----------------\n'
        '| Name            | Use | Amount  |\n'
        '| --------------- | --- | ------- |\n'
        '| Coffee (Brewed) | Keg | 0.71 kg |'
    )

    assert md_weizen.miscs == ''


def test_recipe_mash(md_coffee_stout, md_weizen):
    """Test valid recipe mash table."""
    assert md_coffee_stout.mash == (
        'Mash\n'
        '----\n'
        '| Name     | Type     | Temperature | Time   | Amount  |\n'
        '| -------- | -------- | ----------- | ------ | ------- |\n'
        '| Infusion | Infusion | 152.0 °F    | 60 min | 4.5 gal |'
    )

    md_coffee_stout.temp_unit = 'celsius'
    assert md_coffee_stout.mash == (
        'Mash\n'
        '----\n'
        '| Name     | Type     | Temperature | Time   | Amount  |\n'
        '| -------- | -------- | ----------- | ------ | ------- |\n'
        '| Infusion | Infusion | 66.7 °C     | 60 min | 4.5 gal |'
    )

    md_coffee_stout.vol_unit = 'liters'
    assert md_coffee_stout.mash == (
        'Mash\n'
        '----\n'
        '| Name     | Type     | Temperature | Time   | Amount |\n'
        '| -------- | -------- | ----------- | ------ | ------ |\n'
        '| Infusion | Infusion | 66.7 °C     | 60 min | 17.0 L |'
    )

    assert md_weizen.mash == ''


def test_write_recipes(md_recipes, tmpdir):
    """Test write_recipes function."""
    write_recipes(md_recipes, str(tmpdir))

    for recipe in md_recipes:
        path = tmpdir.join(recipe.filename)
        assert path.read() == recipe.markdown
