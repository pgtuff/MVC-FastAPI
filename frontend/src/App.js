import React, { useState } from 'react';
import './styles/global.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Api from './pages/api';
import Docs from './pages/docs';
import Header from './components/header';
import Footer from './components/footer';

const App = () => {
  // State to manage login status
  const [isLoggedIn, setIsLoggedIn] = useState(true);

  // Function to handle login/logout
  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <Router>
      {/* Pass isLoggedIn and handleLogout to Header */}
      <Header isLoggedIn={isLoggedIn} onLogout={handleLogout} />

      <main style={{ minHeight: '80vh', padding: '20px' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/api" element={<Api />} />
          <Route path="/docs" element={<Docs />} />
        </Routes>
      </main>

      <Footer />
    </Router>
  );
};

export default App;