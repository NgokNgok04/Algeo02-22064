// App.js
import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes,Link } from 'react-router-dom';
import About from './AboutUs';
import HowToUse from './HowtoUse';
import Program from './Program';
import ImageUpload from './components/ImageUpload';

class App extends Component {
  render(){
      return (
        <Router>
          <Routes>
            <Route path="/" element={<Program />}/>
            <Route path="/How-to-Use" element = {<HowToUse />}/>
            <Route path="/about" element={<About />}/>
            <Route exact path = "/upload-image" element={<ImageUpload />} />
          </Routes>
        </Router>
      );
  }
}

export default App;