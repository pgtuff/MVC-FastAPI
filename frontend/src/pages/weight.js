import React from 'react';
import Converter from '../components/converter';

const WeightConverter = () => {
  const units = [
    'kg',
    'g',
    'milligram',
    'metric_ton',
    'long_ton',
    'short_ton',
    'pound',
    'ounce',
    'carat',
    'atomic_mass_unit',
  ].sort();

  return (
    <Converter
      title="Weight Converter"
      units={units}
      defaultFrom="kg"
      defaultTo="g"
    />
  );
};

export default WeightConverter;