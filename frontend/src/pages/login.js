import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js';
import '../styles/global.css';
import '@fortawesome/fontawesome-free/css/all.min.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [agreeToTerms, setAgreeToTerms] = useState(false);
  const [error, setError] = useState(null);
  const [showPassword, setShowPassword] = useState(false);
  const [showTerms, setShowTerms] = useState(false); // State for modal visibility

  const handleLogin = (e) => {
    e.preventDefault();
    if (!agreeToTerms) {
      setError('You must agree to the terms and conditions.');
      return;
    }
    setError(null);
    console.log('Logging in with:', email, password);
    alert(`Login successful for ${email}`);
  };

  const handleGoogleLogin = () => {
    alert('Logging in with Google');
  };

  return (
    <div className="form">
      <form onSubmit={handleLogin} className="form-container">
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '16px' }}>
          <Logo />
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '16px' }}>
          <p>Sign in to your account</p>
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

        <div className="form-row">
          <label htmlFor="password"></label>
          <div style={{ position: 'relative' }}>
            <i className="fa-solid fa-lock" style={{ position: 'absolute', left: '10px', top: '50%', transform: 'translateY(-50%)', color: '#999' }} />
            <input
              type={showPassword ? 'text' : 'password'}
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
              required
              style={{ paddingLeft: '40px', paddingRight: '40px' }}
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              style={{
                position: 'absolute',
                right: '10px',
                top: '50%',
                transform: 'translateY(-75%)',
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                color: '#999',
              }}
            >
              <i className={showPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'} />
            </button>
          </div>
        </div>

        {/* Terms and Conditions Checkbox */}
        <div className="custom-form-row">
          <label>
            <input type="checkbox" checked={agreeToTerms} onChange={(e) => setAgreeToTerms(e.target.checked)} required />
            <button type="button" className="terms-button" onClick={() => setShowTerms(true)}>I agree to the Terms and Conditions</button>
          </label>
        </div>

        {error && <p style={{ color: 'red' }}>Error: {error}</p>}

        <button type="submit" className="cta-button">Login</button>
      </form>

      <div className="text-center">
        <Link to="/forgot-password" className="auth-link">Forgot Password?</Link>
      </div>

      <div className="text-center">
        <p>
          Don't have an account? <Link to="/signup" className="auth-link">Sign Up</Link>
        </p>
      </div>

      <div className="text-center">
        <button onClick={handleGoogleLogin} className="cta-button google-login">Login with Google</button>
      </div>

      {/* Terms and Conditions Modal */}
      {showTerms && (
        <div className="modal">
          <div className="modal-content">
            <span className="close-button" onClick={() => setShowTerms(false)}>&times;</span>
            <h2>Terms and Conditions</h2>
            <p>
              By using this service, you agree to our terms and conditions. You must comply with our policies and guidelines. Violation of these terms may result in account suspension.
            </p>
            <p>
              Your personal data is protected in accordance with our privacy policy. We do not share your information without consent.
            </p>
            <button onClick={() => setShowTerms(false)}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Login;
