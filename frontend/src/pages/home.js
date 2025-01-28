import React from 'react';
import Converter from '../components/converter';

const DistanceConverter = () => {
  const units = [
    'cm',
    'foot',
    'inch',
    'km',
    'light_year',
    'm',
    'micrometer',
    'mile',
    'mm',
    'nanometer',
    'yard',
  ].sort();

  return (
    <Converter
      title="Distance Converter"
      units={units}
      defaultFrom="mile"
      defaultTo="km"
    />
  );
};

export default DistanceConverter;