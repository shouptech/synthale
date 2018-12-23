"""Use this module to parse BeerXML files."""

import os
import re

import pybeerxml


class MarkdownRecipe:
    """A recipe in markdown form."""

    def __init__(self, recipe):
        """Create a MarkdownRecipe object.

        `recipe` is a recipe object from the pybeerxml package.
        """
        self.recipe = recipe

    @property
    def filename(self):
        """Return the filename for the recipe.

        Converts the recipe name to lowercase and replaces all non-word
        characters with an underscore. Trailing underscores are removed.
        `.md` is appended to the name.
        """
        return '{}.md'.format(
            re.sub(
                r'_$', '', re.sub(
                    r'[\W]+', '_', self.recipe.name.lower()
                )
            )
        )

    @property
    def markdown(self):
        """Return generated markdown for the recipe."""
        return ''


def load_file(path):
    """Parse BeerXML file located at `path`.

    Return a list of MarkdownRecipe objects. If an exception is raised during
    parsing, the message is printed to stdout and an empty list is returned.
    """
    try:
        result = pybeerxml.Parser().parse(path)
    except Exception as err:
        print(err)
        return []

    recipes = []
    for recipe in result:
        recipes.append(MarkdownRecipe(recipe))
    return recipes


def load_all_files(path):
    """Parse all files in `path` that end in `.xml`.

    Returns a list of MarkdownRecipe objects.
    """
    recipes = []
    for name in os.listdir(path):
        if name.endswith('.xml'):
            recipes.extend(load_file(os.path.join(path, name)))

    return recipes
