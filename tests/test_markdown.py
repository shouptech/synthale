"""Contains tests for the synthale.markdown module."""
import pytest

from synthale import markdown


@pytest.mark.parametrize('text,level,expected', (
    ('test', 1, 'test\n===='),
    ('foobar', 2, 'foobar\n------'),
    (' test ', None, 'test\n----')
))
def test_setext_heading(text, level, expected):
    """Test for valid setext headings from setext_heading function."""
    assert markdown.setext_heading(text, level) == expected


def test_emphasis():
    """Test emphasis."""
    assert markdown.emphasis('Foo') == '*Foo*'


def test_strong():
    """Test strong."""
    assert markdown.strong('Foo') == '**Foo**'


@pytest.mark.parametrize('headers,rows,expected', (
    (
        ('one', 'two', 'three'),
        (
            ('testing', 'foo', 'bar'),
            ('1', '2', '3'),
        ),
        ('| one     | two | three |\n'
         '| ------- | --- | ----- |\n'
         '| testing | foo | bar   |\n'
         '| 1       | 2   | 3     |'),
    ),
    (
        ('pipe|test',),
        (
            ('testing',),
            ('testin|g',),
        ),
        ('| pipe\\|test |\n'
         '| ---------- |\n'
         '| testing    |\n'
         '| testin\\|g  |')
    )
))
def test_table(headers, rows, expected):
    """Test table generation."""
    assert markdown.table(headers, rows) == expected
