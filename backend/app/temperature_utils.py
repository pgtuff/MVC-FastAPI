class TemperatureConverter:
    # Conversion functions as class-level attributes
    TO_CELSIUS = {
        "celsius": lambda value: value,
        "fahrenheit": lambda value: (value - 32) * 5 / 9,
        "kelvin": lambda value: value - 273.15,
    }

    FROM_CELSIUS = {
        "celsius": lambda value: value,
        "fahrenheit": lambda value: (value * 9 / 5) + 32,
        "kelvin": lambda value: value + 273.15,
    }

    @classmethod
    def temperature_conversion(cls, from_unit, to_unit):
        """
        Are we dealing with a temperature conversion?
        """
        # Normalize units to lowercase
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if from_unit in cls.TO_CELSIUS and to_unit in cls.FROM_CELSIUS:
            return True
        else:
            return False

    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """
        Convert a temperature from one unit to another.

        Args:
            value (float): The temperature to convert.
            from_unit (str): The unit of the input temperature.
            to_unit (str): The unit to convert to.

        Returns:
            float: The converted temperature.
        """
        # Normalize units to lowercase
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in cls.TO_CELSIUS or to_unit not in cls.FROM_CELSIUS:
            raise ValueError(
                f"Unsupported unit. Supported units are: {', '.join(cls.TO_CELSIUS.keys())}"
            )

        # Convert from the source unit to Celsius
        value_in_celsius = cls.TO_CELSIUS[from_unit](value)

        # Convert from Celsius to the target unit
        return cls.FROM_CELSIUS[to_unit](value_in_celsius)
