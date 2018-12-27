"""Contains functions used to convert units.

Input units for volumes is liters. Input units for mass is kilograms. These
units are the defaults used in the BeerXML format, and as a result, in
`pybeerxml`.
"""


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
