"""Use this module to parse BeerXML files."""

import os
import re

import pybeerxml


def parse_xmlfile(path):
    """Parse BeerXML file located at `path`.

    Returns a list of parsed recipes.
    """
    return pybeerxml.Parser().parse(path)


def load_recipes(path):
    """Parse all files in `path` that end in `.xml`.

    Returns a list of parsed recipes.
    """
    recipes = []
    for name in os.listdir(path):
        if name.endswith('.xml'):
            recipes.extend(parse_xmlfile(os.path.join(path, name)))

    return recipes


def name_to_slug(name):
    """Convert a recipe name to a slug.

    Converts the name to lowercase and replaces all non-word characters with an
    underscore. Additionally, removes any trailing underscores.
    """
    return re.sub(r'_$', '', re.sub(r'[\W]+', '_', name.lower()))
