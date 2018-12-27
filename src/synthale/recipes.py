"""Use this module to parse BeerXML files."""

import os
import re
import sys

import pybeerxml

from synthale import markdown, convert


class MarkdownRecipe:
    """A recipe in markdown form."""

    def __init__(self, recipe, vol_unit='gallons', hop_unit='ounces'):
        """Create a MarkdownRecipe object.

        `recipe` is a recipe object from the pybeerxml package.

        `vol_unit` specifies the unit for boil size and batch size. Can be one
        of 'gallons', or 'liters'.

        `hop_unit` specifies the unit for hop amounts. Can be one of
        'ounces', 'pounds', 'grams', or 'kilograms'. If specified unit is not
        matched, default is 'ounces'.
        """
        self.recipe = recipe
        self.vol_unit = vol_unit
        self.hop_unit = hop_unit

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
            self.details,
            '',
            self.hops,
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

    @property
    def details(self):
        """Return markdown for the recipe's details."""
        if self.vol_unit == 'gallons':
            boil_size = convert.gallons(self.recipe.boil_size, '.1f')
            batch_size = convert.gallons(self.recipe.batch_size, '.1f')
        else:
            boil_size = convert.liters(self.recipe.boil_size, '.1f')
            batch_size = convert.liters(self.recipe.batch_size, '.1f')

        return '\n'.join((
            markdown.setext_heading('Details', 2),
            '{}: {}'.format(markdown.strong('Type'), self.recipe.type),
            '{}: {:.1f} %'.format(markdown.strong('Batch efficiency'),
                                  self.recipe.efficiency),
            '{}: {}'.format(markdown.strong('Boil size'), boil_size),
            '{}: {} min'.format(markdown.strong('Boil length'),
                                int(self.recipe.boil_time)),
            '{}: {}'.format(markdown.strong('Batch size'), batch_size),
            '{}: {:.3f}'.format(markdown.strong('Estimated OG'),
                                self.recipe.og),
            '{}: {:.3f}'.format(markdown.strong('Estimated FG'),
                                self.recipe.fg),
            '{}: {}'.format(markdown.strong('Estimated IBU'),
                            int(self.recipe.ibu)),
            '{}: {:.1f}'.format(markdown.strong('Estimated SRM'),
                                self.recipe.color),
            '{}: {:.1f} %'.format(markdown.strong('Estimated ABV'),
                                  self.recipe.abv)
        ))

    @property
    def hops(self):
        """Return markdown to represent the recipe's hops."""
        headers = ('Name', 'Origin', 'Alpha', 'Amount', 'Time', 'Use')
        rows = []
        for hop in self.recipe.hops:
            if self.hop_unit == 'pounds':
                amt = convert.pounds(hop.amount, '.2f')
            elif self.hop_unit == 'grams':
                amt = convert.grams(hop.amount, '.1f')
            elif self.hop_unit == 'kilograms':
                amt = convert.kilograms(hop.amount, '.2f')
            else:
                amt = convert.ounces(hop.amount, '.1f')
            rows.append((
                hop.name,
                hop.origin,
                '{:.1f} %'.format(hop.alpha),
                amt,
                '{}'.format(int(round(hop.time))),
                hop.use,
            ))
        return (
            '{}\n{}'.format(
                markdown.setext_heading('Hops', level=2),
                markdown.table(headers, rows)
            )
        )


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
