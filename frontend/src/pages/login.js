import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [agreeToTerms, setAgreeToTerms] = useState(false);

  const handleLogin = (e) => {
    e.preventDefault();
    if (!agreeToTerms) {
      alert('You must agree to the terms and conditions.');
      return;
    }
    // Add login logic here (e.g., API call to authenticate user)
    console.log('Logging in with:', email, password);
    alert(`Login successful for ${email}`);
  };

  const handleGoogleLogin = () => {
    // Add Google login logic here (e.g., Firebase or OAuth)
    alert('Logging in with Google');
  };

  return (
    <div className="container">
      <h1>Login</h1>
      <p>Sign in to your account or create a new one.</p>

      {/* Login Form */}
      <form onSubmit={handleLogin} className="form-container">
        <div className="form-row">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            required
          />
        </div>

        <div className="form-row">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
          />
        </div>

        <div className="form-row">
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

export default Login