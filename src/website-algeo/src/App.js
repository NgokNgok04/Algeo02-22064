// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes,Link } from 'react-router-dom';
import Home from './Home';
import About from './AboutUs';
import HowToUse from './HowtoUse';
import Program from './Program';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Reverse-Image-Search" element={<Program />}/>
        <Route path="/How-to-Use" element = {<HowToUse />}/>
        <Route path="/about" element={<About />}/>
      </Routes>
    </Router>
  );
};

export default App;