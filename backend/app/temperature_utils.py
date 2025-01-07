# temperature_converter.py

from .unit_converter import UnitConverter

class TemperatureConverter(UnitConverter):
    TO_BASE_UNIT = {
        "celsius": lambda value: value,
        "fahrenheit": lambda value: (value - 32) * 5 / 9,
        "kelvin": lambda value: value - 273.15,
    }

    FROM_BASE_UNIT = {
        "celsius": lambda value: value,
        "fahrenheit": lambda value: (value * 9 / 5) + 32,
        "kelvin": lambda value: value + 273.15,
    }
