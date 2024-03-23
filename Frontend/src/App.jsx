import React from 'react';
import Navbar from './components/Navbar';
import Slider from './components/Slider';
import DescriptionSection from './components/Footer';

function App() {
  return (
    <div id='body'>
      <Navbar />
      <Slider />
      <DescriptionSection />
    </div>
  );
}

export default App;
