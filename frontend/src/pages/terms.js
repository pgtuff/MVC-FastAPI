import React from 'react';
import { Link } from 'react-router-dom';
import Logo from '../components/logo.js';
import '../styles/global.css';

const TermsAndConditions = () => {
  return (
    <div className="container">
      <div className="center" style={{ marginBottom: '32px' }}>
        <Logo />
      </div>

      <h1 className="text-center">Terms and Conditions</h1>

      <div className="form-container" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', backgroundColor: '#fff', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)' }}>
        <h2>1. Introduction</h2>
        <p>
          Welcome to ConvertAnyUnit ("we," "our," "us"). These Terms and Conditions govern your use of our website located at ConvertAnyUnit.com (the "Website") and any related services provided by us.
        </p>
        <p>
          By accessing or using the Website, you agree to be bound by these Terms and Conditions. If you disagree with any part of these terms, you must not use the Website.
        </p>

        <h2>2. Intellectual Property Rights</h2>
        <p>
          Unless otherwise stated, we own the intellectual property rights for all material on the Website. All intellectual property rights are reserved. You may access this material for your personal use, subject to the restrictions set out in these Terms and Conditions.
        </p>

        <h2>3. Restrictions</h2>
        <p>
          You are specifically restricted from:
        </p>
        <ul>
          <li>Republishing material from the Website without our prior written consent.</li>
          <li>Selling, renting, or sub-licensing material from the Website.</li>
          <li>Using the Website in any way that is, or may be, damaging to the Website or our business.</li>
          <li>Engaging in any data mining, data harvesting, or similar activities.</li>
        </ul>

        <h2>4. Your Content</h2>
        <p>
          In these Terms and Conditions, "Your Content" refers to any audio, video, text, images, or other material you choose to display on the Website. By displaying Your Content, you grant us a non-exclusive, worldwide, irrevocable license to use, reproduce, adapt, and publish it for the purposes of operating and promoting the Website.
        </p>

        <h2>5. Limitation of Liability</h2>
        <p>
          To the fullest extent permitted by law, we shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits, data, or use, whether in an action in contract, tort, or otherwise, arising out of or in any way connected with your use of the Website.
        </p>

        <h2>6. Governing Law</h2>
        <p>
          These Terms and Conditions are governed by and construed in accordance with the laws of England and Wales. Any disputes relating to these terms will be subject to the exclusive jurisdiction of the courts of England and Wales.
        </p>

        <h2>7. Changes to These Terms</h2>
        <p>
          We reserve the right to modify these Terms and Conditions at any time. Any changes will be effective immediately upon posting on the Website. Your continued use of the Website after any changes constitutes your acceptance of the new Terms and Conditions.
        </p>

        <h2>8. Contact Us</h2>
        <p>
          If you have any questions about these Terms and Conditions, please contact us at:
        </p>
        <p>
          Email: <a href="mailto:support@convertanyunit.com" className="terms-link">support@convertanyunit.com</a><br />
        </p>
      </div>

      <div className="text-center" style={{ marginTop: '32px' }}>
        <Link to="/" className="cta-button">Back to Home</Link>
      </div>
    </div>
  );
};

export default TermsAndConditions;