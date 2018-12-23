"""This module contains functions to generate markdown elements."""


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
