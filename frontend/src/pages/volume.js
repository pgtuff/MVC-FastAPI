import React from 'react';
import Converter from '../components/converter';

const VolumeConverter = () => {
  const units = [
    "cubic_m",
    "cubic_km",
    "cubic_cm",
    "cubic_mm",
    "litre",
    "millilitre",
    "us_gallon",
    "us_quart",
    "us_pint",
    "us_cup",
    "us_fluid_ounce",
    "us_table_spoon",
    "us_tea_spoon",
    "imperial_gallon",
    "imperial_quart",
    "imperial_pint",
    "imperial_fluid_ounce",
    "imperial_table_spoon",
    "imperial_tea_spoon",
    "cubic_mile",
    "cubic_yard",
    "cubic_foot",
    "cubic_inch",
  ].sort(); // Alphabetically sort the units

  return (
    <Converter
      title="Volume Converter"
      units={units}
      defaultFrom="litre"
      defaultTo="millilitre"
    />
  );
};

export default VolumeConverter;
