import pytest
from backend.app.area_utils import AreaConverter

def test_convert_square_m_to_square_km():
    assert pytest.approx(AreaConverter.convert(1_000_000, "square_m", "square_km")) == 1
    assert pytest.approx(AreaConverter.convert(10_000_000, "square_m", "square_km")) == 10

def test_convert_square_km_to_square_m():
    assert pytest.approx(AreaConverter.convert(1, "square_km", "square_m")) == 1_000_000
    assert pytest.approx(AreaConverter.convert(0.5, "square_km", "square_m")) == 500_000

def test_convert_square_m_to_acre():
    assert pytest.approx(AreaConverter.convert(4046.8564224, "square_m", "acre")) == 1
    assert pytest.approx(AreaConverter.convert(8093.7128448, "square_m", "acre")) == 2

def test_convert_acre_to_square_m():
    assert pytest.approx(AreaConverter.convert(1, "acre", "square_m")) == 4046.8564224
    assert pytest.approx(AreaConverter.convert(2, "acre", "square_m")) == 8093.7128448

def test_convert_square_foot_to_square_inch():
    assert pytest.approx(AreaConverter.convert(1, "square_foot", "square_inch")) == 144
    assert pytest.approx(AreaConverter.convert(10, "square_foot", "square_inch")) == 1440

def test_convert_square_inch_to_square_foot():
    assert pytest.approx(AreaConverter.convert(144, "square_inch", "square_foot")) == 1
    assert pytest.approx(AreaConverter.convert(720, "square_inch", "square_foot")) == 5

def test_convert_square_mile_to_square_yard():
    assert pytest.approx(AreaConverter.convert(1, "square_mile", "square_yard")) == 3_097_600
    assert pytest.approx(AreaConverter.convert(0.5, "square_mile", "square_yard")) == 1_548_800

def test_convert_square_yard_to_square_mile():
    assert pytest.approx(AreaConverter.convert(3_097_600, "square_yard", "square_mile")) == 0.9999992704
    assert pytest.approx(AreaConverter.convert(1_548_800, "square_yard", "square_mile")) == 0.5

def test_invalid_conversion():
    with pytest.raises(ValueError, match="Unsupported unit"):
        AreaConverter.convert(100, "invalid_unit", "square_m")
    with pytest.raises(ValueError, match="Unsupported unit"):
        AreaConverter.convert(100, "square_m", "invalid_unit")
