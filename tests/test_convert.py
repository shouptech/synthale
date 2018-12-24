"""Contains tests for the synthale.convert module."""

from synthale.convert import liters, gallons


def test_liters():
    """Test liters function."""
    assert liters(1, '.1f') == '1.0 L'


def test_gallons():
    """Test gallons function."""
    assert gallons(1, '.1f') == '0.3 gal'
