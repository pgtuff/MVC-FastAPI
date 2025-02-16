import React, { useState } from 'react';
import './styles/global.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Api from './pages/api';
import Docs from './pages/docs';
import WeightConverter from './pages/weight'; // Import the WeightConverter component
import AreaConverter from './pages/area';
import TemperatureConverter from './pages/temperature';
import TimeConverter from './pages/time';
import VolumeConverter from './pages/volume';
import Login from './pages/login';
import Profile from './pages/profile';
import Header from './components/header';
import ForgotPassword from './pages/forgot-password';
import Footer from './components/footer';
import SignUp from './pages/signup';
import TermsAndConditions from './pages/terms';


const App = () => {
  // State to manage login status
  const [isLoggedIn, setIsLoggedIn] = useState(false);

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
          <Route path="/weight" element={<WeightConverter />} /> {/* Add WeightConverter route */}
          <Route path="/area" element={<AreaConverter />} />
          <Route path="/temperature" element={<TemperatureConverter />} />
          <Route path="/time" element={<TimeConverter />} />
          <Route path="/volume" element={<VolumeConverter />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/terms" element={<TermsAndConditions />} />
        </Routes>
      </main>

      <Footer />
    </Router>
  );
};

export default App;