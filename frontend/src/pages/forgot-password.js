import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js';
import '../styles/global.css';
import '@fortawesome/fontawesome-free/css/all.min.css';

const ForgotPassword = () => {
  const [email, setEmail] = useState('');
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!email) {
      setError('Please enter your email address.');
      return;
    }
    setError(null);
    // Simulate a successful password reset request
    setSuccess(true);
    console.log('Password reset requested for:', email);
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit} className="form-container">
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '16px' }}>
          <Logo />
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '16px' }}>
          <p>Forgot your password?</p>
        </div>

        <div className="form-row">
          <label htmlFor="email"></label>
          <div style={{ position: 'relative' }}>
            <i className="fa-regular fa-envelope" style={{ position: 'absolute', left: '10px', top: '50%', transform: 'translateY(-50%)', color: '#999' }}></i>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
              className="email-input"
              style={{ paddingLeft: '40px' }}
            />
          </div>
        </div>

        {error && <p style={{ color: 'red' }}>Error: {error}</p>}
        {success && <p style={{ color: 'green' }}>Password reset instructions have been sent to your email.</p>}

        <button type="submit" className="cta-button">Reset Password</button>

        <div className="terms-text">
          <Link to="/login" className="terms-link">Back to Login</Link>
        </div>
      </form>
    </div>
  );
};

export default ForgotPassword;