import React from 'react';
import { NavLink } from 'react-router-dom'; // Use NavLink instead of Link
import Logo from '../components/logo.js'; // Adjust the import path if needed

const Header = ({ isLoggedIn }) => {
  return (
    <header className="header">
      {/* Top row with logo, main links, and auth options */}
      <nav className="nav-links">
        {/* Logo link with a specific class to exclude it from active styling */}
        <NavLink to="/" className="nav-link logo-link" exact>
          <Logo />
        </NavLink>

        {/* Other nav links */}
        <NavLink to="/about" className="nav-link" activeClassName="active">
          About
        </NavLink>
        <NavLink to="/api" className="nav-link" activeClassName="active">
          Get API Access
        </NavLink>
        <NavLink to="/docs" className="nav-link" activeClassName="active">
          API Docs
        </NavLink>

        {/* Auth links on the right-hand side */}
        <div className="auth-links">
          {isLoggedIn ? (
            <NavLink to="/profile" className="auth-link" activeClassName="active">
              Profile
            </NavLink>
          ) : (
            <NavLink to="/login" className="auth-link" activeClassName="active">
              Sign In
            </NavLink>
          )}
        </div>
      </nav>

      {/* New row for unit conversion links */}
      <nav className="unit-links">
        <NavLink to="/" className="unit-link" activeClassName="active" exact>
          Distance
        </NavLink>
        <NavLink to="/weight" className="unit-link" activeClassName="active">
          Weight
        </NavLink>
        <NavLink to="/volume" className="unit-link" activeClassName="active">
          Volume
        </NavLink>
        <NavLink to="/area" className="unit-link" activeClassName="active">
          Area
        </NavLink>
        <NavLink to="/temperature" className="unit-link" activeClassName="active">
          Temperature
        </NavLink>
        <NavLink to="/time" className="unit-link" activeClassName="active">
          Time
        </NavLink>
      </nav>
    </header>
  );
};

export default Header;