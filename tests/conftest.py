"""Contains fixtures used during tests."""

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
