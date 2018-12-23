"""Contains tests for the synthale.markdown module."""
import pytest

from synthale import markdown


@pytest.mark.parametrize('text,level,expected', [
    ('test', 1, 'test\n===='),
    ('foobar', 2, 'foobar\n------'),
    (' test ', None, 'test\n----')
])
def test_setext_heading(text, level, expected):
    """Test for valid setext headings from setext_heading function."""
    assert markdown.setext_heading(text, level) == expected
