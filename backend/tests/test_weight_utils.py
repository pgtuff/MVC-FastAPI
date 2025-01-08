import pytest
from backend.app.weight_utils import WeightConverter

def test_convert_kg_to_g():
    assert pytest.approx(WeightConverter.convert(1, "kg", "g")) == 1000
    assert pytest.approx(WeightConverter.convert(2, "kg", "g")) == 2000

def test_convert_g_to_kg():
    assert pytest.approx(WeightConverter.convert(1000, "g", "kg")) == 1
    assert pytest.approx(WeightConverter.convert(2000, "g", "kg")) == 2

def test_convert_kg_to_pound():
    assert pytest.approx(WeightConverter.convert(1, "kg", "pound")) == 2.20462262
    assert pytest.approx(WeightConverter.convert(2, "kg", "pound")) == 4.40924524

def test_convert_pound_to_kg():
    assert pytest.approx(WeightConverter.convert(2.20462262, "pound", "kg")) == 1
    assert pytest.approx(WeightConverter.convert(4.40924524, "pound", "kg")) == 2

def test_convert_kg_to_ounce():
    assert pytest.approx(WeightConverter.convert(1, "kg", "ounce")) == 35.27396195
    assert pytest.approx(WeightConverter.convert(2, "kg", "ounce")) == 70.5479239

def test_convert_ounce_to_kg():
    assert pytest.approx(WeightConverter.convert(35.27396195, "ounce", "kg")) == 1
    assert pytest.approx(WeightConverter.convert(70.5479239, "ounce", "kg")) == 2

def test_convert_kg_to_long_ton():
    assert pytest.approx(WeightConverter.convert(1000, "kg", "long_ton")) == 0.9842065
    assert pytest.approx(WeightConverter.convert(2000, "kg", "long_ton")) == 1.968413

def test_convert_long_ton_to_kg():
    assert pytest.approx(WeightConverter.convert(0.9842065, "long_ton", "kg")) == 1000
    assert pytest.approx(WeightConverter.convert(1.968413, "long_ton", "kg")) == 2000

def test_convert_kg_to_short_ton():
    assert pytest.approx(WeightConverter.convert(1000, "kg", "short_ton")) == 1.1023113
    assert pytest.approx(WeightConverter.convert(2000, "kg", "short_ton")) == 2.2046226

def test_convert_short_ton_to_kg():
    assert pytest.approx(WeightConverter.convert(1.1023113, "short_ton", "kg")) == 1000
    assert pytest.approx(WeightConverter.convert(2.2046226, "short_ton", "kg")) == 2000

def test_invalid_conversion():
    with pytest.raises(ValueError, match="Unsupported unit"):
        WeightConverter.convert(100, "invalid_unit", "kg")
    with pytest.raises(ValueError, match="Unsupported unit"):
        WeightConverter.convert(100, "kg", "invalid_unit")
