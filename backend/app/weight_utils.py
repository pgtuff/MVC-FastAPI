# weight_converter.py

from .unit_converter import UnitConverter

class WeightConverter(UnitConverter):
    TO_BASE_UNIT = {
        "kg": lambda value: value,
        "g": lambda value: value / 1000,
        "milligram": lambda value: value / 1_000_000,
        "metric_ton": lambda value: value * 1000,
        "long_ton": lambda value: value * 1016.0469088,
        "short_ton": lambda value: value * 907.18474,
        "pound": lambda value: value * 0.45359237,
        "ounce": lambda value: value * 0.028349523125,
        "carat": lambda value: value / 5000,
        "atomic_mass_unit": lambda value: value * 1.66053906660e-27,
    }

    FROM_BASE_UNIT = {
        "kg": lambda value: value,
        "g": lambda value: value * 1000,
        "milligram": lambda value: value * 1_000_000,
        "metric_ton": lambda value: value / 1000,
        "long_ton": lambda value: value / 1016.0469088,
        "short_ton": lambda value: value / 907.18474,
        "pound": lambda value: value / 0.45359237,
        "ounce": lambda value: value / 0.028349523125,
        "carat": lambda value: value * 5000,
        "atomic_mass_unit": lambda value: value / 1.66053906660e-27,
    }
