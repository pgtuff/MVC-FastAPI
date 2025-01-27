import React from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js'; // Adjust the import path if needed

const Header = ({ isLoggedIn }) => {
  return (
    <header className="header">
      {/* Top row with logo, main links, and auth options */}
      <nav className="nav-links">
        <Link to="/" className="nav-link"><Logo /></Link>
        <Link to="/about" className="nav-link">About</Link>
        <Link to="/api" className="nav-link">Get API Access</Link>
        <Link to="/docs" className="nav-link">API Docs</Link>
        
        {/* Auth links on the right-hand side */}
        <div className="auth-links">
          {isLoggedIn ? (
            <Link to="/profile" className="auth-link">Profile</Link>
          ) : (
            <Link to="/login" className="auth-link">Sign In</Link>
          )}
        </div>
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