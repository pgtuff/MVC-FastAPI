# unit_converter.py

class UnitConverter:
    TO_BASE_UNIT = {}
    FROM_BASE_UNIT = {}

    @classmethod
    def is_supported_conversion(cls, from_unit, to_unit):
        """
        Check if the conversion between the given units is supported.

        Args:
            from_unit (str): The source unit.
            to_unit (str): The target unit.

        Returns:
            bool: True if the conversion is supported, False otherwise.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        return from_unit in cls.TO_BASE_UNIT and to_unit in cls.FROM_BASE_UNIT

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a value from one unit to another.

        Args:
            value (float): The value to convert.
            from_unit (str): The unit of the input value.
            to_unit (str): The unit to convert to.

        Returns:
            float: The converted value.
        """
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if not cls.is_supported_conversion(from_unit, to_unit):
            raise ValueError(
                f"Unsupported unit. Supported units are: {', '.join(cls.TO_BASE_UNIT.keys())}"
            )

        # Convert from the source unit to the base unit
        value_in_base_unit = cls.TO_BASE_UNIT[from_unit](value)

        # Convert from the base unit to the target unit
        return cls.FROM_BASE_UNIT[to_unit](value_in_base_unit)
