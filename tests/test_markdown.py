"""Contains tests for the synthale.markdown module."""

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
