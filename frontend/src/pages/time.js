import React from 'react';
import Converter from '../components/converter';

const TimeConverter = () => {
  const units = [
    "second",
    "millisecond",
    "microsecond",
    "nanosecond",
    "picosecond",
    "minute",
    "hour",
    "day",
    "week",
    "month",
    "year",
  ].sort((a, b) => a.localeCompare(b)); // Alphabetically sort the units

  return (
    <Converter
      title="Time Converter"
      units={units}
      defaultFrom="second"
      defaultTo="minute"
    />
  );
};

export default TimeConverter;
