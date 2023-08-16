import React, { useEffect, useRef, useState } from 'react';
import ReactSlider from 'react-slider';

import '../../styles/Slider.css';
import background0 from'../../styles/visualAssets/background0.jpg';
import background1 from'../../styles/visualAssets/background1.jpg';
import background2 from'../../styles/visualAssets/background2.jpg';

const Slider = ({title}) => {
    const [slideIndex, setSlideIndex] = useState(1);
    const [width, height] = useWindowSize();
    // Get the position and ref of the div element from the custom hook
    const [position, ref] = useDivPosition();
    const images = [ background0, background1, background2 ];

    // Define the style object for the div element
    const sliderStyle = {
      width: width,
      height: height,
      overflow: "hidden",
      position: "relative",
    };
    const imageStyle = {
      width: "auto",
      height: "auto",
      minWidth: "100%",
      minHeight: "100%",
      transform: `translate(${-position.x}px, ${-position.y}px)`,
    };

    return (
      <div style={sliderStyle} ref={ref}>
        <img src={images[slideIndex - 1]} alt="Image" style={imageStyle} />
        <h1 className='floating-title'>{title()}</h1>
      </div>
    );
}
export default Slider;

function useWindowSize() {
  const [size, setSize] = React.useState([window.innerWidth, window.innerHeight]);
  useEffect(() => {
    const handleResize = () => {
      setSize([window.innerWidth, window.innerHeight]);
    };
    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  return size;
}

// A custom hook that returns the current position of the div element
function useDivPosition() {
  const [position, setPosition] = React.useState({ x: 0, y: 0 });
  const divRef = useRef(null);

  useEffect(() => {
    // Get the dimensions of the div element and the image
    const div = divRef.current;
    const img = div.querySelector("img");
    const divWidth = div.offsetWidth;
    const divHeight = div.offsetHeight;
    const imgWidth = img.naturalWidth;
    const imgHeight = img.naturalHeight;

    // Calculate the maximum values for x and y
    const viewPortWidth = imgWidth - divWidth;
    const viewPortHeight = imgHeight - divHeight;

    // Define a function that updates the position of the div element
    const updatePosition = () => {
      const currentTimeInMs = Date.now();
      const newPositionAsAPercentage = Math.cos(currentTimeInMs / 100000) * 0.5 + 0.5;
      const x = newPositionAsAPercentage * viewPortWidth;
      const y = newPositionAsAPercentage * viewPortHeight;

      setPosition({ x, y });
    };

    // Call the function once to initialize the position
    updatePosition();

    // Set an interval to update the position every 50 milliseconds
    const intervalId = setInterval(updatePosition, 50);

    // Return a cleanup function that clears the interval
    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return [position, divRef];
}


// <h1 className='shadow'>{title()}</h1>

// const nextSlide = () => {
//     if(slideIndex !== images.length){
//         setSlideIndex(slideIndex + 1);
//     } else if (slideIndex === images.length){
//         setSlideIndex(1);
//     }
// }
//
// const prevSlide = () => {
//     if(slideIndex !== 1){
//         setSlideIndex(slideIndex - 1);
//     } else if (slideIndex === 1) {
//         setSlideIndex(images.length);
//     }
// }
//
// const moveDot = (index) => {
//     setSlideIndex(index);
// }
//
// const titleText = title();
//
// console.log('render title: %s', title());
// const imageStyle = { backgroundImage: background0 };
//
// console.log('Slider render slideIndex: %s', slideIndex);
// return (
//   <div className='slide' style={imageStyle}>
//     <div className='floating-title'>
//       <h1 className='title'>{titleText}</h1>
//       <h1 className='shadow'>{titleText}</h1>
//     </div>
//   </div>
// )
// <div className='slideshow'>
//   <img src={images[slideIndex - 1]}/>
// </div>
// <div className='slideshow'>
//   <BtnSlider moveSlide={prevSlide} direction={'prev'} />
//   <BtnSlider moveSlide={nextSlide} direction={'next'} />
// </div>
// <div className='container-dots'>
//     {Array.from({length: 5}).map((item, index) => (
//         <div
//           onClick={() => moveDot(index + 1)}
//           className={slideIndex === index + 1 ? 'dot active' : 'dot'}
//         ></div>
//     ))}
// </div>
// // {images.map((obj, index) => {
//     return (
//         <Slide
//           className={slideIndex === index + 1 ? 'slide active-anim' : 'slide'}
//           title={title}
//           image={obj}
//         />
//     )
// })}
