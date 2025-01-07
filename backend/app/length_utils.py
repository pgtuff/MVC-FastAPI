# length_converter.py

from .unit_converter import UnitConverter

class LengthConverter(UnitConverter):
    TO_BASE_UNIT = {
        "mm": lambda value: value / 1000,
        "cm": lambda value: value / 100,
        "m": lambda value: value,
        "km": lambda value: value * 1000,
        "micrometer": lambda value: value / 1e6,
        "nanometer": lambda value: value / 1e9,
        "yard": lambda value: value * 0.9144,
        "foot": lambda value: value * 0.3048,
        "mile": lambda value: value * 1609.344,
        "inch": lambda value: value * 0.0254,
        "light_year": lambda value: value * 9.461e15,
    }

    FROM_BASE_UNIT = {
        "mm": lambda value: value * 1000,
        "cm": lambda value: value * 100,
        "m": lambda value: value,
        "km": lambda value: value / 1000,
        "micrometer": lambda value: value * 1e6,
        "nanometer": lambda value: value * 1e9,
        "yard": lambda value: value / 0.9144,
        "foot": lambda value: value / 0.3048,
        "mile": lambda value: value / 1609.344,
        "inch": lambda value: value / 0.0254,
        "light_year": lambda value: value / 9.461e15,
    }
