import pytest
from backend.app.temperature_utils import TemperatureConverter

def test_convert_celsius_to_fahrenheit():
    assert pytest.approx(TemperatureConverter.convert(0, "celsius", "fahrenheit")) == 32
    assert pytest.approx(TemperatureConverter.convert(100, "celsius", "fahrenheit")) == 212
    assert pytest.approx(TemperatureConverter.convert(-40, "celsius", "fahrenheit")) == -40

def test_convert_celsius_to_kelvin():
    assert pytest.approx(TemperatureConverter.convert(0, "celsius", "kelvin")) == 273.15
    assert pytest.approx(TemperatureConverter.convert(-273.15, "celsius", "kelvin")) == 0
    assert pytest.approx(TemperatureConverter.convert(100, "celsius", "kelvin")) == 373.15

def test_convert_fahrenheit_to_celsius():
    assert pytest.approx(TemperatureConverter.convert(32, "fahrenheit", "celsius")) == 0
    assert pytest.approx(TemperatureConverter.convert(212, "fahrenheit", "celsius")) == 100
    assert pytest.approx(TemperatureConverter.convert(-40, "fahrenheit", "celsius")) == -40

def test_convert_fahrenheit_to_kelvin():
    assert pytest.approx(TemperatureConverter.convert(32, "fahrenheit", "kelvin")) == 273.15
    assert pytest.approx(TemperatureConverter.convert(212, "fahrenheit", "kelvin")) == 373.15
    assert pytest.approx(TemperatureConverter.convert(-459.67, "fahrenheit", "kelvin")) == 0

def test_convert_kelvin_to_celsius():
    assert pytest.approx(TemperatureConverter.convert(273.15, "kelvin", "celsius")) == 0
    assert pytest.approx(TemperatureConverter.convert(0, "kelvin", "celsius")) == -273.15
    assert pytest.approx(TemperatureConverter.convert(373.15, "kelvin", "celsius")) == 100

def test_convert_kelvin_to_fahrenheit():
    assert pytest.approx(TemperatureConverter.convert(273.15, "kelvin", "fahrenheit")) == 32
    assert pytest.approx(TemperatureConverter.convert(373.15, "kelvin", "fahrenheit")) == 212
    assert pytest.approx(TemperatureConverter.convert(0, "kelvin", "fahrenheit")) == -459.67

def test_invalid_conversion():
    with pytest.raises(ValueError, match="Unsupported unit"):
        TemperatureConverter.convert(100, "invalid_unit", "celsius")
    with pytest.raises(ValueError, match="Unsupported unit"):
        TemperatureConverter.convert(100, "celsius", "invalid_unit")
