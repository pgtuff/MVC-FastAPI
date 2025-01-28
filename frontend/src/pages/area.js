import React from 'react';
import Converter from '../components/converter';

const AreaConverter = () => {
  const units = [
    "square_m",
    "square_km",
    "square_cm",
    "square_mm",
    "square_micrometer",
    "square_mile",
    "square_yard",
    "square_foot",
    "square_inch",
    "acre",
  ].sort(); // Alphabetically sort the units

  return (
    <Converter
      title="Area Converter"
      units={units}
      defaultFrom="square_m"
      defaultTo="square_km"
    />
  );
};

export default AreaConverter;
