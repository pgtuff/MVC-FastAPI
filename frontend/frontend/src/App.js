import React, { useState, useEffect } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [items, setItems] = useState([]);

  // Fetch data from the FastAPI backend
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/items/")
      .then((response) => {
        setItems(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Items from FastAPI Backend</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name}: ${item.price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
