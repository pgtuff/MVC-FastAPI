import React, { useState } from 'react';

const Home = () => {
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleButtonClick = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/generate_http_key', {
        method: 'GET', // Change to POST if the endpoint requires it
      });
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }
      const data = await res.json();
      setResponse(data); // Assuming the response is JSON
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h1>Home Page</h1>
      <button onClick={handleButtonClick}>Generate HTTP Key</button>
      {response && <p>Response: {JSON.stringify(response)}</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

export default Home;
