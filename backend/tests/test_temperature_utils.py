import pytest
from backend.app.temperature_utils import *

def test_celsius_to_fahrenheit():
    assert pytest.approx(celsius_to_fahrenheit(0)) == 32
    assert pytest.approx(celsius_to_fahrenheit(100)) == 212
    assert pytest.approx(celsius_to_fahrenheit(-40)) == -40

def test_celsius_to_kelvin():
    assert pytest.approx(celsius_to_kelvin(0)) == 273.15
    assert pytest.approx(celsius_to_kelvin(-273.15)) == 0
    assert pytest.approx(celsius_to_kelvin(100)) == 373.15

def test_fahrenheit_to_celsius():
    assert pytest.approx(fahrenheit_to_celsius(32)) == 0
    assert pytest.approx(fahrenheit_to_celsius(212)) == 100
    assert pytest.approx(fahrenheit_to_celsius(-40)) == -40

def test_fahrenheit_to_kelvin():
    assert pytest.approx(fahrenheit_to_kelvin(32)) == 273.15
    assert pytest.approx(fahrenheit_to_kelvin(212)) == 373.15
    assert pytest.approx(fahrenheit_to_kelvin(-459.67)) == 0

def test_kelvin_to_celsius():
    assert pytest.approx(kelvin_to_celsius(273.15)) == 0
    assert pytest.approx(kelvin_to_celsius(0)) == -273.15
    assert pytest.approx(kelvin_to_celsius(373.15)) == 100

def test_kelvin_to_fahrenheit():
    assert pytest.approx(kelvin_to_fahrenheit(273.15)) == 32
    assert pytest.approx(kelvin_to_fahrenheit(373.15)) == 212
    assert pytest.approx(kelvin_to_fahrenheit(0)) == -459.67
