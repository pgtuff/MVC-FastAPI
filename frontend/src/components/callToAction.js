import React from 'react';
import { Link } from 'react-router-dom'; // Assuming you're using React Router for navigation
import '../styles/global.css'; // Import global styles

const CallToAction = () => {
  return (
    <div className="cta-container">
      <p className="cta-text">
        Get API access and unlock powerful features today!
      </p>
      <Link to="/get-api-access" className="cta-button">
        Get API Access
      </Link>
    </div>
  );
};

export default CallToAction;