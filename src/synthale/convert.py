"""Contains functions used to convert units.

Input units for volumes is liters. Input units for mass is kilograms. These
units are the defaults used in the BeerXML format, and as a result, in
`pybeerxml`.
"""

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


def liters(liters, format_spec=''):
    """Return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} L').format(liters)


def gallons(liters, format_spec=''):
    """Convert liters to gallons and return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} gal').format(liters * 0.264178)


def kilograms(kilograms, format_spec=''):
    """Return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} kg').format(kilograms)


def grams(kilograms, format_spec=''):
    """Convert kilograms to grams and return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} g').format(kilograms * 1000.0)


def ounces(kilograms, format_spec=''):
    """Convert kilograms to ounces and return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} oz').format(kilograms * 35.273962)


def pounds(kilograms, format_spec=''):
    """Convert kilograms to pounds and return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} lb').format(kilograms * 2.204623)


def celsius(celsius, format_spec=''):
    """Return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} °C').format(celsius)


def fahrenheit(celsius, format_spec=''):
    """Convert celsius to fahrenheit and return a string with the unit appended.

    See  the `Format Specification Mini-Language
    <https://docs.python.org/3/library/string.html#format-specification-mini-language>_`
    for how to write `format_spec`.
    """
    return ('{:' + format_spec + '} °F').format(celsius * 1.8 + 32)
