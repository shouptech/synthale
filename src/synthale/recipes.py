"""Use this module to parse BeerXML files."""

import os
import re
import sys

import pybeerxml

from synthale import markdown


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
        return '\n'.join((
            self.name,
            '',
            self.style,
            '',
        ))

    @property
    def name(self):
        """Return markdown for the recipe's name."""
        return markdown.setext_heading(self.recipe.name, 1)

    @property
    def style(self):
        """Return markdown for the recipe's style."""
        return '\n'.join((
            markdown.setext_heading('Style', 2),
            '{}: {}'.format(markdown.strong('Style guide'),
                            self.recipe.style.style_guide),
            '{}: {}{}'.format(markdown.strong('Style category'),
                              int(self.recipe.style.category_number),
                              self.recipe.style.style_letter),
            '{}: {}'.format(markdown.strong('Style name'),
                            self.recipe.style.name)
        ))


def load_file(path):
    """Parse BeerXML file located at `path`.

    Return a list of MarkdownRecipe objects. If an exception is raised during
    parsing, the message is printed to stderr and an empty list is returned.
    """
    try:
        result = pybeerxml.Parser().parse(path)
    except Exception as err:
        print('Error parsing {}: {}'.format(path, err), file=sys.stderr)
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


def write_recipes(recipes, output_path):
    """Write `recipes` to `output_path`.

    `recipes` is a list of MarkdownRecipe objects. `output_path` is a directory
    to write the recipes to.
    """
    for recipe in recipes:
        with open(os.path.join(output_path, recipe.filename), 'w') as f:
            f.write(recipe.markdown)
