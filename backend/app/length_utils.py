class LengthConverter:
    # Conversion functions as class-level attributes
    TO_METERS = {
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

    FROM_METERS = {
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

    @classmethod
    def length_conversion(cls, from_unit, to_unit):
        """
        Are we dealing with a length conversion?
        """
        # Normalize units to lowercase
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit in cls.TO_METERS and to_unit in cls.FROM_METERS:
            return True
        else:
            return False

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a length from one unit to another.

        Args:
            value (float): The length to convert.
            from_unit (str): The unit of the input length.
            to_unit (str): The unit to convert to.

        Returns:
            float: The converted length.
        """
        # Normalize units to lowercase
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in cls.TO_METERS or to_unit not in cls.FROM_METERS:
            raise ValueError(
                f"Unsupported unit. Supported units are: {', '.join(cls.TO_METERS.keys())}"
            )

        # Convert from the source unit to meters
        value_in_meters = cls.TO_METERS[from_unit](value)

        # Convert from meters to the target unit
        return cls.FROM_METERS[to_unit](value_in_meters)