import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js';
import '../styles/global.css';
import '@fortawesome/fontawesome-free/css/all.min.css';

const Login = () => {
  const [email, setEmail] = useState(''); // Email input
  const [password, setPassword] = useState(''); // Password input
  const [agreeToTerms, setAgreeToTerms] = useState(false); // Terms agreement checkbox
  const [error, setError] = useState(null); // Error handling
  const [showPassword, setShowPassword] = useState(false); // Toggle password visibility

  const handleLogin = (e) => {
    e.preventDefault();
    if (!agreeToTerms) {
      setError('You must agree to the terms and conditions.');
      return;
    }
    setError(null); // Clear any previous errors

    // Add login logic here (e.g., API call to authenticate user)
    console.log('Logging in with:', email, password);
    alert(`Login successful for ${email}`);
  };

  const handleGoogleLogin = () => {
    // Add Google login logic here (e.g., Firebase or OAuth)
    alert('Logging in with Google');
  };

  return (
    <div className="form">
      {/* Login Form */}
      <form onSubmit={handleLogin} className="form-container">
        {/* Centered Logo */}
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '16px' }}>
          <Logo />
        </div>

        {/* Centered Title */}
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '16px' }}>
          <p>Sign in to your account</p>
        </div>

        {/* Email Input */}
        <div className="form-row">
          <label htmlFor="email"></label>
          <div style={{ position: 'relative' }}>
            {/* Font Awesome Email Icon */}
            <i
              className="fa-regular fa-envelope"
              style={{
                position: 'absolute',
                left: '10px',
                top: '50%',
                transform: 'translateY(-50%)',
                color: '#999',
              }}
            ></i>
            {/* Email Input Field */}
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
              className="email-input"
              style={{ paddingLeft: '40px' }} // Add padding to avoid text overlap
            />
          </div>
        </div>

        {/* Password Input */}
        <div className="form-row">
          <label htmlFor="password"></label>
          <div style={{ position: 'relative' }}>
            {/* Font Awesome Lock Icon */}
            <i
              className="fa-solid fa-lock"
              style={{
                position: 'absolute',
                left: '10px',
                top: '50%',
                transform: 'translateY(-50%)',
                color: '#999',
              }}
            />
            {/* Password Input Field */}
            <input
              type={showPassword ? 'text' : 'password'} // Toggle input type
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
              required
              style={{ paddingLeft: '40px', paddingRight: '40px' }} // Add padding for the toggle button
            />
            {/* Password Visibility Toggle Button */}
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
            <input
              type="checkbox"
              checked={agreeToTerms}
              onChange={(e) => setAgreeToTerms(e.target.checked)}
              required
            />
            I agree to the <Link to="/terms">Terms and Conditions</Link>
          </label>
        </div>

        {/* Error Message */}
        {error && <p style={{ color: 'red' }}>Error: {error}</p>}

        {/* Login Button */}
        <button type="submit" className="cta-button">
          Login
        </button>
      </form>

      {/* Forgot Password Link */}
      <div className="text-center">
        <Link to="/forgot-password" className="auth-link">
          Forgot Password?
        </Link>
      </div>

      {/* Sign Up Option */}
      <div className="text-center">
        <p>
          Don't have an account?{' '}
          <Link to="/signup" className="auth-link">
            Sign Up
          </Link>
        </p>
      </div>

      {/* Login with Google Button */}
      <div className="text-center">
        <button onClick={handleGoogleLogin} className="cta-button google-login">
          Login with Google
        </button>
      </div>
    </div>
  );
};

export default Login;