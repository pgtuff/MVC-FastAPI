import pytest
from backend.app.length_utils import LengthConverter  # Import the LengthConverter class

# Test cases for the LengthConverter.convert method
def test_convert_length():
    assert pytest.approx(LengthConverter.convert(1000, "mm", "m")) == 1
    assert pytest.approx(LengthConverter.convert(1, "km", "m")) == 1000
    assert pytest.approx(LengthConverter.convert(1, "m", "cm")) == 100
    assert pytest.approx(LengthConverter.convert(1e6, "micrometer", "m")) == 1
    assert pytest.approx(LengthConverter.convert(1, "yard", "m")) == 0.9144
    assert pytest.approx(LengthConverter.convert(1, "foot", "inch")) == 12
    assert pytest.approx(LengthConverter.convert(1, "mile", "km")) == 1.609344
    assert pytest.approx(LengthConverter.convert(1, "light_year", "m")) == 9.461e15
    assert pytest.approx(LengthConverter.convert(1, "m", "m")) == 1

def test_convert_length_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported unit"):
        LengthConverter.convert(1, "invalid_unit", "m")

    with pytest.raises(ValueError, match="Unsupported unit"):
        LengthConverter.convert(1, "m", "invalid_unit")

# Optional: Add more specific test cases for each unit conversion
def test_convert_mm_to_m():
    assert pytest.approx(LengthConverter.convert(1000, "mm", "m")) == 1

def test_convert_cm_to_m():
    assert pytest.approx(LengthConverter.convert(100, "cm", "m")) == 1

def test_convert_m_to_mm():
    assert pytest.approx(LengthConverter.convert(1, "m", "mm")) == 1000

def test_convert_km_to_m():
    assert pytest.approx(LengthConverter.convert(1, "km", "m")) == 1000

def test_convert_m_to_km():
    assert pytest.approx(LengthConverter.convert(1000, "m", "km")) == 1

def test_convert_mile_to_km():
    assert pytest.approx(LengthConverter.convert(1, "mile", "km")) == 1.609344

def test_convert_m_to_light_year():
    assert pytest.approx(LengthConverter.convert(9.461e15, "m", "light_year")) == 1

# Additional test cases for edge cases
def test_convert_case_insensitivity():
    assert pytest.approx(LengthConverter.convert(1000, "MM", "m")) == 1
    assert pytest.approx(LengthConverter.convert(1, "Km", "M")) == 1000
