"""Contains fixtures used during tests."""

import pytest
import pybeerxml

from synthale.recipes import MarkdownRecipe


@pytest.fixture
def xml_recipes():
    """Generate a list of pybeerxml.Recipe objects."""
    coffeestout = pybeerxml.Parser().parse('tests/recipes/coffee-stout.xml')[0]
    weizen = pybeerxml.Parser().parse('tests/recipes/weizen.xml')[0]
    return [coffeestout, weizen]


@pytest.fixture
def md_recipes():
    """Generate a list of MarkdownRecipe objects."""
    coffeestout = pybeerxml.Parser().parse('tests/recipes/coffee-stout.xml')[0]
    weizen = pybeerxml.Parser().parse('tests/recipes/weizen.xml')[0]
    return [MarkdownRecipe(coffeestout), MarkdownRecipe(weizen)]


@pytest.fixture
def md_weizen():
    """Return the sample weizen recipe as a MarkdownRecipe object."""
    return MarkdownRecipe(
        pybeerxml.Parser().parse('tests/recipes/weizen.xml')[0]
    )


@pytest.fixture
def md_coffee_stout():
    """Return the sample coffee stout recipe as a MarkdownRecipe object."""
    return MarkdownRecipe(
        pybeerxml.Parser().parse('tests/recipes/coffee-stout.xml')[0]
    )
