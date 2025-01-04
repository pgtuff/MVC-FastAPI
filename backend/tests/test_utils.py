import pytest
from backend.app.length_utils import *  # Import the function to test

# Test cases for individual conversion functions
def test_mm_to_m():
    assert pytest.approx(mm_to_m(1000)) == 1

def test_cm_to_m():
    assert pytest.approx(cm_to_m(100)) == 1

def test_m_to_m():
    assert pytest.approx(m_to_m(1)) == 1

def test_km_to_m():
    assert pytest.approx(km_to_m(1)) == 1000

def test_micrometer_to_m():
    assert pytest.approx(micrometer_to_m(1e6)) == 1

def test_nanometer_to_m():
    assert pytest.approx(nanometer_to_m(1e9)) == 1

def test_yard_to_m():
    assert pytest.approx(yard_to_m(1)) == 0.9144

def test_foot_to_m():
    assert pytest.approx(foot_to_m(1)) == 0.3048

def test_mile_to_m():
    assert pytest.approx(mile_to_m(1)) == 1609.34

def test_inch_to_m():
    assert pytest.approx(inch_to_m(1)) == 0.0254

def test_light_year_to_m():
    assert pytest.approx(light_year_to_m(1)) == 9.461e15

def test_m_to_mm():
    assert pytest.approx(m_to_mm(1)) == 1000

def test_m_to_cm():
    assert pytest.approx(m_to_cm(1)) == 100

def test_m_to_km():
    assert pytest.approx(m_to_km(1000)) == 1

def test_m_to_micrometer():
    assert pytest.approx(m_to_micrometer(1)) == 1e6

def test_m_to_nanometer():
    assert pytest.approx(m_to_nanometer(1)) == 1e9

def test_m_to_yard():
    assert pytest.approx(m_to_yard(0.9144)) == 1

def test_m_to_foot():
    assert pytest.approx(m_to_foot(0.3048)) == 1

def test_m_to_mile():
    assert pytest.approx(m_to_mile(1609.34)) == 1

def test_m_to_inch():
    assert pytest.approx(m_to_inch(0.0254)) == 1

def test_m_to_light_year():
    assert pytest.approx(m_to_light_year(9.461e15)) == 1

# Test cases for the convert_length function
def test_convert_length():
    assert pytest.approx(convert_length(1000, "mm", "m")) == 1
    assert pytest.approx(convert_length(1, "km", "m")) == 1000
    assert pytest.approx(convert_length(1, "m", "cm")) == 100
    assert pytest.approx(convert_length(1e6, "micrometer", "m")) == 1
    assert pytest.approx(convert_length(1, "yard", "m")) == 0.9144
    assert pytest.approx(convert_length(1, "foot", "inch")) == 12
    assert pytest.approx(convert_length(1, "mile", "km")) == 1.60934
    assert pytest.approx(convert_length(1, "light_year", "m")) == 9.461e15
    assert pytest.approx(convert_length(1, "m", "m")) == 1

def test_convert_length_invalid_unit():
    with pytest.raises(ValueError, match="Unsupported unit"):
        convert_length(1, "invalid_unit", "m")

    with pytest.raises(ValueError, match="Unsupported unit"):
        convert_length(1, "m", "invalid_unit")
