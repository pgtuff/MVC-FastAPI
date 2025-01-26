import React from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js'; // Adjust the path if needed

const Header = () => {
  return (
    <header className="header">
      <nav className="nav-links">
        <Link to="/" className="nav-link"><Logo /></Link>
        <Link to="/about" className="nav-link">About</Link>
        <Link to="/contact" className="nav-link">Contact</Link>
      </nav>
    </header>
  );
};

export default Header;
