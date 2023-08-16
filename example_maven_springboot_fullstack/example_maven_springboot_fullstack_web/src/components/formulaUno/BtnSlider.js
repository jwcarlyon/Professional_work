import React from 'react';
// import './Slider.css';

import leftArrow from '../../styles/visualAssets/leftArrow.png';
import rightArrow from '../../styles/visualAssets/rightArrow.png';

export default function BtnSlider({ direction, moveSlide }) {

  console.log(direction, moveSlide);

  return (
    <button
      onClick={moveSlide}
      className={direction === 'next' ? 'btn-slide next' : 'btn-slide prev'}
    >
      <img src={direction === 'next' ? rightArrow : leftArrow} />
    </button>
  );

};
