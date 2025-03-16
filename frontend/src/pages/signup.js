import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js';
import '../styles/global.css';
import '@fortawesome/fontawesome-free/css/all.min.css';

const SignUp = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [agreeToTerms, setAgreeToTerms] = useState(false);
  const [error, setError] = useState(null);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const handleSignUp = async (e) => {
    e.preventDefault();

    // Validation
    if (!email || !password || !confirmPassword) {
      setError('Please fill in all fields.');
      return;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }

    if (!agreeToTerms) {
      setError('You must agree to the terms and conditions.');
      return;
    }

    setError(null);

    // Send data to the backend
    try {
      const response = await fetch('http://localhost:8000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          password,
          confirm_password: confirmPassword,
          agree_to_terms: agreeToTerms,
        }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || 'Sign-up failed.');
      }

      const data = await response.json();
      alert(`Sign-up successful for ${data.email}`);
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="form-container center">
      <form onSubmit={handleSignUp} className="form-container">
        <div className="center" style={{ marginBottom: '16px' }}>
          <Logo />
        </div>

        <div className="center" style={{ marginBottom: '16px' }}>
          <h2>Create a new account</h2>
        </div>

        {/* Email Input */}
        <div className="form-row">
          <div style={{ position: 'relative' }}>
            <i className="fa-regular fa-envelope" style={{ position: 'absolute', left: '10px', top: '50%', transform: 'translateY(-50%)', color: '#999' }}></i>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
              style={{ paddingLeft: '40px' }}
            />
          </div>
        </div>

        {/* Password Input */}
        <div className="form-row">
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

        {/* Confirm Password Input */}
        <div className="form-row">
          <div style={{ position: 'relative' }}>
            <i className="fa-solid fa-lock" style={{ position: 'absolute', left: '10px', top: '50%', transform: 'translateY(-50%)', color: '#999' }} />
            <input
              type={showConfirmPassword ? 'text' : 'password'}
              id="confirmPassword"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm your password"
              required
              style={{ paddingLeft: '40px', paddingRight: '40px' }}
            />
            <button
              type="button"
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
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
              <i className={showConfirmPassword ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye'} />
            </button>
          </div>
        </div>

        {/* Terms and Conditions Checkbox */}
        <div className="custom-form-row">
          <label>
            <input
              type="checkbox"
              checked={agreeToTerms}
              onChange={(e) => setAgreeToTerms(e.target.checked)}
              required
            />
            <span className="terms-text">
              <Link to="/terms" className="terms-link">I agree to the Terms and Conditions</Link>
            </span>
          </label>
        </div>

        {/* Error Message */}
        {error && <p style={{ color: 'red', textAlign: 'center' }}>Error: {error}</p>}

        {/* Sign Up Button */}
        <button type="submit" className="cta-button">Sign Up</button>

        {/* Links to Login and Forgot Password */}
        <div className="terms-text">
          <Link to="/login" className="terms-link left-link">Already have an account? Login</Link>
        </div>
      </form>
    </div>
  );
};

export default SignUp;