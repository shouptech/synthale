"""Use this module to parse BeerXML files."""

# Copyright (C) 2019 Mike Shoup
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import re
import sys

import pybeerxml

from synthale import markdown, convert


class MarkdownRecipe:
    """A recipe in markdown form."""

    def __init__(self,
                 recipe,
                 vol_unit='gallons',
                 hop_unit='ounces',
                 fermentable_unit='pounds',
                 temp_unit='fahrenheit'):
        """Create a MarkdownRecipe object.

        `recipe` is a recipe object from the pybeerxml package.

        `vol_unit` specifies the unit for boil size and batch size. Can be one
        of 'gallons', or 'liters'. If specified unit is not matched, default is
        'liters'.

        `hop_unit` specifies the unit for hop amounts. Can be one of
        'ounces', 'pounds', 'grams', or 'kilograms'. If specified unit is not
        matched, default is 'ounces'.

        `fermentable_unit` specifies the unit for fermentable amounts. Can be
        one of 'ounces', 'pounds', 'grams', or 'kilograms'. If specified unit
        is not matched, default is 'pounds'.

        `temp_unit` specifies the unit for temperatures. Can be one of
        'fahrenheit' or 'celsius'. If specified unit is not matched, default is
        'fahrenheit'.
        """
        self.recipe = recipe
        self.vol_unit = vol_unit
        self.hop_unit = hop_unit
        self.fermentable_unit = fermentable_unit
        self.temp_unit = temp_unit

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
        md = '\n'.join((
            self.name,
            '',
            self.style,
            '',
            self.details,
            '',
            self.fermentables,
            '',
            self.hops,
            '',
            self.yeast,
            '',
        ))

        if len(self.miscs) > 0:
            md += '\n'.join(('', self.miscs, '',))

        if len(self.mash) > 0:
            md += '\n'.join(('', self.mash, '',))

        return md

    @property
    def name(self):
        """Return markdown for the recipe's name."""
        return markdown.setext_heading(self.recipe.name, 1)

    @property
    def style(self):
        """Return markdown for the recipe's style."""
        heading = markdown.setext_heading('Style', 2) + '\n'
        return heading + '\\\n'.join((
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

        heading = markdown.setext_heading('Details', 2) + '\n'

        return heading + '\\\n'.join((
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
    def fermentables(self):
        """Return markdown to represent the recipe's fermentables."""
        headers = ('Name', 'Type', 'Color', 'Amount')
        rows = []
        for fermentable in self.recipe.fermentables:
            if self.fermentable_unit == 'ounces':
                amt = convert.ounces(fermentable.amount, '.1f')
            elif self.fermentable_unit == 'grams':
                amt = convert.grams(fermentable.amount, '.1f')
            elif self.fermentable_unit == 'kilograms':
                amt = convert.kilograms(fermentable.amount, '.2f')
            else:
                amt = convert.pounds(fermentable.amount, '.2f')
            rows.append((
                fermentable.name,
                fermentable.type,
                '{:.1f} °L'.format(fermentable.color),
                amt
            ))
        return (
            '{}\n{}'.format(
                markdown.setext_heading('Fermentables', level=2),
                markdown.table(headers, rows)
            )
        )

    @property
    def hops(self):
        """Return markdown to represent the recipe's hops."""
        headers = ('Name', 'Origin', 'Alpha', 'Amount', 'Time', 'Use')
        rows = []
        for hop in self.recipe.hops:
            # Determine hop unit
            if self.hop_unit == 'pounds':
                amt = convert.pounds(hop.amount, '.2f')
            elif self.hop_unit == 'grams':
                amt = convert.grams(hop.amount, '.1f')
            elif self.hop_unit == 'kilograms':
                amt = convert.kilograms(hop.amount, '.2f')
            else:
                amt = convert.ounces(hop.amount, '.1f')

            # Determine hop timing
            if hop.use == 'Dry Hop':
                # 1 day = 1440 minutes
                time = '{:.1f} days'.format(hop.time / 1440.0)
            else:
                time = '{} min'.format(int(round(hop.time)))
            rows.append((
                hop.name,
                hop.origin,
                '{:.1f} %'.format(hop.alpha),
                amt,
                time,
                hop.use,
            ))
        return (
            '{}\n{}'.format(
                markdown.setext_heading('Hops', level=2),
                markdown.table(headers, rows)
            )
        )

    @property
    def yeast(self):
        """Return markdown to represent the recipe's yeast."""
        headers = ('Name', 'Lab', 'Type', 'Attenuation')
        rows = []
        for yeast in self.recipe.yeasts:
            rows.append((
                yeast.name,
                yeast.laboratory,
                yeast.type,
                '{:.1f} %'.format(yeast.attenuation),
            ))
        return (
            '{}\n{}'.format(
                markdown.setext_heading('Yeast', level=2),
                markdown.table(headers, rows)
            )
        )

    @property
    def miscs(self):
        """Return the markdown to represent the recipe's other ingredients."""
        if len(self.recipe.miscs) == 0:
            return ''

        headers = ('Name', 'Use', 'Amount')
        rows = []
        for misc in self.recipe.miscs:
            if misc.display_amount is not None:
                amt = str(misc.display_amount)
            elif misc.amount_is_weight:
                amt = '{:.2f} kg'.format(misc.amount)
            else:
                amt = '{:.2f} L'.format(misc.amount)
            rows.append((
                misc.name,
                misc.use,
                amt
            ))
        return (
            '{}\n{}'.format(
                markdown.setext_heading('Other Ingredients', level=2),
                markdown.table(headers, rows)
            )
        )

    @property
    def mash(self):
        """Return the markdown to represent the recipe's mash steps."""
        if self.recipe.mash is None:
            return ''

        headers = ('Name', 'Type', 'Temperature', 'Time', 'Amount')
        rows = []
        for step in self.recipe.mash.steps:
            if self.temp_unit == 'celsius':
                temp = convert.celsius(step.step_temp, '.1f')
            else:
                temp = convert.fahrenheit(step.step_temp, '.1f')
            if self.vol_unit == 'gallons':
                amt = convert.gallons(step.infuse_amount, '.1f')
            else:
                amt = convert.liters(step.infuse_amount, '.1f')
            rows.append((
                step.name,
                step.type,
                temp,
                '{} min'.format(int(step.step_time)),
                amt
            ))
        return (
            '{}\n{}'.format(
                markdown.setext_heading('Mash', level=2),
                markdown.table(headers, rows)
            )
        )


def load_file(path, units={}):
    """Parse BeerXML file.

    `path` is the path to a BeerXML file. `units` is a dictionary defining
    the units used. `units` will be unpacked and used during the creation of a
    `MarkdownRecipe` object.

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
        recipes.append(MarkdownRecipe(recipe, **units))
    return recipes


def load_all_files(path, units={}):
    """Parse all XML files in a directory.

    `path` is a path to a directory with .xml files. `units` is a dictionary
    defining the units used. `units` will be unpacked and used during the
    creation of a `MarkdownRecipe` object.

    Returns a list of MarkdownRecipe objects.
    """
    recipes = []
    for name in os.listdir(path):
        if name.endswith('.xml'):
            recipes.extend(load_file(os.path.join(path, name), units))

    return recipes


def write_recipes(recipes, output_path):
    """Write `recipes` to `output_path`.

    `recipes` is a list of MarkdownRecipe objects. `output_path` is a directory
    to write the recipes to.
    """
    for recipe in recipes:
        with open(os.path.join(output_path, recipe.filename), 'w') as f:
            f.write(recipe.markdown)
