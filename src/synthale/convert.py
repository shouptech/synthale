"""Contains functions used to convert units."""


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
