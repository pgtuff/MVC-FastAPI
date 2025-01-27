import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Api from './pages/api';
import Api from './pages/docs';

const AppRoutes = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/api" element={<Api />} />
      <Route path="/docs" element={<Docs />} />
    </Routes>
  </Router>
);

export default AppRoutes;
