import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import About from './pages/about';
import Api from './pages/api';
import Docs from './pages/docs';
import WeightConverter from '../pages/weight'; // Import WeightConverter
import AreaConverter from '../pages/area';
import TemperatureConverter from '../pages/temperature';
import TimeConverter from '../pages/time';
import VolumeConverter from '../pages/volume';

const AppRoutes = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} /> {/* Home page */}
      <Route path="/about" element={<About />} />
      <Route path="/api" element={<Api />} />
      <Route path="/docs" element={<Docs />} />
      <Route path="/weight" element={<WeightConverter />} /> {/* WeightConverter route */}
      <Route path="/area" element={<AreaConverter />} />
      <Route path="/temperature" element={<TemperatureConverter />} />
      <Route path="/time" element={<TimeConverter />} />
      <Route path="/volume" element={<VolumeConverter />} />
    </Routes>
  </Router>
);

export default AppRoutes;