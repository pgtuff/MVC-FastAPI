import React from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js'; // Adjust the path if needed

const Header = () => {
  return (
    <header className="header">
      {/* Top row with logo and main links */}
      <nav className="nav-links">
        <Link to="/" className="nav-link"><Logo /></Link>
        <Link to="/about" className="nav-link">About</Link>
        <Link to="/contact" className="nav-link">Contact</Link>
      </nav>

      {/* New row for unit conversion links */}
      <nav className="unit-links">
        <Link to="/" className="unit-link">Distance</Link>
        <Link to="/weight" className="unit-link">Weight</Link>
        <Link to="/volume" className="unit-link">Volume</Link>
        <Link to="/area" className="unit-link">Area</Link>
        <Link to="/temperature" className="unit-link">Temperature</Link>
        <Link to="/time" className="unit-link">Time</Link>
      </nav>
    </header>
  );
};

export default Header;