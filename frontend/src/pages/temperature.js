import React from 'react';
import Converter from '../components/converter';

const TemperatureConverter = () => {
  const units = [
    "celsius",
    "fahrenheit",
    "kelvin",
  ].sort((a, b) => a.localeCompare(b)); // Alphabetically sort the units

  return (
    <Converter
      title="Temperature Converter"
      units={units}
      defaultFrom="celsius"
      defaultTo="fahrenheit"
    />
  );
};

export default TemperatureConverter;
