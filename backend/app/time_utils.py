# time_converter.py

from .unit_converter import UnitConverter

class TimeConverter(UnitConverter):
    TO_BASE_UNIT = {
        "second": lambda value: value,
        "millisecond": lambda value: value / 1000,
        "microsecond": lambda value: value / 1_000_000,
        "nanosecond": lambda value: value / 1_000_000_000,
        "picosecond": lambda value: value / 1_000_000_000_000,
        "minute": lambda value: value * 60,
        "hour": lambda value: value * 3600,
        "day": lambda value: value * 86400,
        "week": lambda value: value * 604800,
        "month": lambda value: value * 2_629_746,
        "year": lambda value: value * 31_557_600,
    }

    def seconds_to_months(value):
        # Round not working in the lambda.
        return round(value / 2_629_746)

    def seconds_to_years(value):
        # Round not working in the lambda.
        return round(value / 31_557_600)
    
    FROM_BASE_UNIT = {
        "second": lambda value: value,
        "millisecond": lambda value: value * 1000,
        "microsecond": lambda value: value * 1_000_000,
        "nanosecond": lambda value: value * 1_000_000_000,
        "picosecond": lambda value: value * 1_000_000_000_000,
        "minute": lambda value: value / 60,
        "hour": lambda value: value / 3600,
        "day": lambda value: value / 86400,
        "week": lambda value: value / 604800,
        "month": seconds_to_months,
        "year": seconds_to_years,
    }
