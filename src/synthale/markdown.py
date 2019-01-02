"""This module contains functions to generate markdown elements."""

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

import re


def setext_heading(text, level):
    """Return an setext heading.

    `text` is the text to include in the heading. Leading and trailing
    whitespace is trimmed from `text`. If `level` is the number `1`, a first
    level (h1) heading is returned. If `level` is the number `2` (or anything
    else), a second level (h2) heading is returned.

    See https://github.github.com/gfm/#setext-heading for more information.
    """
    if level == 1:
        hchar = '='
    else:
        hchar = '-'

    return '{}\n{}'.format(text.strip(), hchar * len(text.strip()))


def emphasis(text):
    """Wrap text with asterisks."""
    return '*{}*'.format(text)


def strong(text):
    """Wrap text with double asterisks."""
    return '**{}**'.format(text)


def table(headers, rows):
    """Generate a table.

    `headers` is a list/tuple of header cells. `rows` is a list of lists
    containing each cell. If any row has more cells than there are headers, the
    extra cells are silently dropped.

    See https://github.github.com/gfm/#tables-extension- for syntax of a GFM
    table.
    """
    colwidth = []  # Tuple to store width of columns
    for idx, val in enumerate(headers):
        # Pad each column with spaces and count pipes (they get escaped)
        colwidth.insert(idx, len(val) + 1 + val.count('|'))

    # Find max width for each column
    for row in rows:
        for idx, val in enumerate(row):
            if len(val) + 1 + val.count('|') > colwidth[idx]:
                colwidth[idx] = len(val) + 1 + val.count('|')

    # Header row
    table = '|'
    for idx, val in enumerate(headers):
        table += ' {}{}|'.format(
            re.sub(r'\|', r'\|', val),
            ' ' * (colwidth[idx] - len(val) - val.count('|'))
        )

    # Delimiter row
    table += '\n|'
    for width in colwidth:
        table += ' {} |'.format('-' * (width - 1))

    # Table rows
    for row in rows:
        table += '\n|'
        for idx, val in enumerate(row):
            table += ' {}{}|'.format(
                re.sub(r'\|', r'\|', val),
                ' ' * (colwidth[idx] - len(val) - val.count('|'))
            )

    return table
