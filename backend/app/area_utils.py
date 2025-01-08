from .unit_converter import UnitConverter

class AreaConverter(UnitConverter):
    TO_BASE_UNIT = {
        "square_m": lambda value: value,  # Base unit is square meters
        "square_km": lambda value: value * 1e6,
        "square_cm": lambda value: value / 1e4,
        "square_mm": lambda value: value / 1e6,
        "square_micrometer": lambda value: value / 1e12,
        "square_mile": lambda value: value * 2589988.11,
        "square_yard": lambda value: value * 0.83612736,
        "square_foot": lambda value: value * 0.092903,
        "square_inch": lambda value: value * 0.00064516,
        "acre": lambda value: value * 4046.8564224,
    }

    FROM_BASE_UNIT = {
        "square_m": lambda value: value,
        "square_km": lambda value: value / 1e6,
        "square_cm": lambda value: value * 1e4,
        "square_mm": lambda value: value * 1e6,
        "square_micrometer": lambda value: value * 1e12,
        "square_mile": lambda value: value / 2_589_988.11,
        "square_yard": lambda value: value / 0.836127,
        "square_foot": lambda value: value / 0.092903,
        "square_inch": lambda value: value / 0.00064516,
        "acre": lambda value: value / 4046.8564224,
    }
