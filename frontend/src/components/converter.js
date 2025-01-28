import React, { useState } from 'react';
import CallToAction from '../components/callToAction'; // Import the CallToAction component
import '../styles/global.css';

const Converter = ({ title, units, defaultFrom, defaultTo }) => {
  const [sourceValue, setSourceValue] = useState(''); // Source value input
  const [decimalPoints, setDecimalPoints] = useState(''); // Optional decimal points input
  const [convertFrom, setConvertFrom] = useState(defaultFrom); // Default source unit
  const [convertTo, setConvertTo] = useState(defaultTo); // Default destination unit
  const [response, setResponse] = useState(null); // Result of conversion
  const [error, setError] = useState(null); // Error handling

  const handleConvert = async () => {
    if (!sourceValue) {
      setError('Please enter a source value.');
      return;
    }
    setError(null); // Clear any previous errors

    try {
      const url = new URL('http://127.0.0.1:8000/convert_value');
      url.searchParams.append('convert_from', convertFrom);
      url.searchParams.append('convert_to', convertTo);
      url.searchParams.append('source_value', sourceValue);
      url.searchParams.append('decimal_points', decimalPoints || '2');

      const res = await fetch(url.toString(), {
        method: 'GET',
        headers: {
          Authorization: 'Bearer your-secret-key', // Pass API key in the header
        },
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data); // Set the entire response object
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="form-container">
      <h1>{title}</h1>
      <div className="form-row">
        <label htmlFor="source-value">Source Value:</label>
        <input
          id="source-value"
          type="number"
          value={sourceValue}
          onChange={(e) => setSourceValue(e.target.value)}
          placeholder="Enter value"
        />
      </div>
      <div className="form-row">
        <label htmlFor="convert-from">Convert From:</label>
        <select
          id="convert-from"
          value={convertFrom}
          onChange={(e) => setConvertFrom(e.target.value)}
        >
          {units.map((unit) => (
            <option key={unit} value={unit}>
              {unit}
            </option>
          ))}
        </select>
      </div>
      <div className="form-row">
        <label htmlFor="convert-to">Convert To:</label>
        <select
          id="convert-to"
          value={convertTo}
          onChange={(e) => setConvertTo(e.target.value)}
        >
          {units.map((unit) => (
            <option key={unit} value={unit}>
              {unit}
            </option>
          ))}
        </select>
      </div>
      <div className="form-row">
        <label htmlFor="decimal-points">Decimal Points (Optional):</label>
        <input
          id="decimal-points"
          type="number"
          value={decimalPoints}
          onChange={(e) => setDecimalPoints(e.target.value)}
          placeholder="Defaults to 2"
        />
      </div>
      <button onClick={handleConvert}>Convert</button>
      {response !== null && (
        <p>
          Result: <strong>{response.result} {response.unit}</strong>
        </p>
      )}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      {/* Add the CallToAction component here */}
      <CallToAction />
    </div>
  );
};

export default Converter;