"""Contains tests for the synthale.convert module."""

from synthale import convert


def test_liters():
    """Test liters function."""
    assert convert.liters(1, '.1f') == '1.0 L'


def test_gallons():
    """Test gallons function."""
    assert convert.gallons(1, '.1f') == '0.3 gal'


def test_kilograms():
    """Test kilograms function."""
    assert convert.kilograms(1, '.1f') == '1.0 kg'


def test_grams():
    """Test grams function."""
    assert convert.grams(1, '.1f') == '1000.0 g'


def test_ounces():
    """Test ounces function."""
    assert convert.ounces(1, '.1f') == '35.3 oz'


def test_pounds():
    """Test pounds function."""
    assert convert.pounds(1, '.1f') == '2.2 lb'


def test_celsius():
    """Test celsius function."""
    assert convert.celsius(1, '.1f') == '1.0 °C'


def test_fahrenheit():
    """Test fahrenheit function."""
    assert convert.fahrenheit(1, '.1f') == '33.8 °F'
