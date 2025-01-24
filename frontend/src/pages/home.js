import React, { useState } from 'react';

const Home = () => {
  const [sourceValue, setSourceValue] = useState(''); // Source value input
  const [decimalPoints, setDecimalPoints] = useState('2'); // Optional decimal points input
  const [convertFrom, setConvertFrom] = useState('mile'); // Default source unit
  const [convertTo, setConvertTo] = useState('km'); // Default destination unit
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
          'Authorization': 'Bearer your-secret-key', // Pass API key in the header
        },
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data.result); // Assuming the API returns { "result": <value> }
    } catch (err) {
      setError(err.message);
    }
  };

  const units = [
    'mm',
    'cm',
    'm',
    'km',
    'micrometer',
    'nanometer',
    'yard',
    'foot',
    'mile',
    'inch',
    'light_year',
  ];

  return (
    <div>
      <h1>Unit Converter</h1>
      <div>
        <label htmlFor="source-value">Source Value:</label>
        <input
          id="source-value"
          type="number"
          value={sourceValue}
          onChange={(e) => setSourceValue(e.target.value)}
          placeholder="Enter value"
        />
      </div>
      <div>
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
      <div>
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
      <div>
        <label htmlFor="decimal-points">Decimal Points (Optional):</label>
        <input
          id="decimal-points"
          type="number"
          value={decimalPoints}
          onChange={(e) => setDecimalPoints(e.target.value)}
          placeholder="e.g., 2"
        />
      </div>
      <button onClick={handleConvert}>Convert</button>
      {response !== null && (
        <p>
          Result: <strong>{response}</strong>
        </p>
      )}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

export default Home;
