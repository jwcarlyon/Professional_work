import React, { useEffect, useRef, useState } from 'react';
import ReactSlider from 'react-slider';
import {connect} from 'react-redux';

import withRouter from '../utils/routerWrapper';
import DriverStatsTicker from '../drivers/DriverStatsTicker';
import '../../styles/Slider.css';
import background0 from'../../styles/visualAssets/background0.jpg';
import background1 from'../../styles/visualAssets/background1.jpg';
import background2 from'../../styles/visualAssets/background2.jpg';

export const Slider = (props) => {
    const {title} = props;
    const [screenEdgeTimeoutInMs, setTimeout] = useState(0);
    const [currentTimeInMs, setTime] = useState(Date.now());
    const [slideIndex, setSlideIndex] = useState(1);
    const images = [ background0, background1, background2 ];

    const useWindowSize = () => {
        const [size, setSize] = React.useState([window.innerWidth, window.innerHeight]);
        useEffect(() => {
            const handleResize = () => {
                setSize([window.innerWidth, window.innerHeight]);
            };
            window.addEventListener('resize', handleResize);

            return () => {
                  window.removeEventListener('resize', handleResize);
            };
        }, []);
        return size;
    }
    const [width, height] = useWindowSize();

    const useDivPosition = (setTime) => {
        const [position, setPosition] = React.useState({ x: 0, y: 0 });
        const divRef = useRef(null);

        useEffect(() => {
            const div = divRef.current;
            const img = div.querySelector('img');
            const divWidth = div.offsetWidth;
            const divHeight = div.offsetHeight;
            const imgWidth = img.naturalWidth;
            const imgHeight = img.naturalHeight;
            // Calculate the maximum values for x and y
            const viewPortWidth = imgWidth - divWidth;
            const viewPortHeight = imgHeight - divHeight;
            const updatePosition = () => {
                const currentTimeInMs = Date.now();
                setTime(currentTimeInMs);
                const timeDerivative = .5 + (Math.abs(Math.cos(currentTimeInMs / 100000)) / 2);
                const x = viewPortWidth - (timeDerivative * viewPortWidth);
                const y = viewPortHeight - (timeDerivative * viewPortHeight);

                setPosition({ x, y });
            };
            updatePosition();
            const intervalId = setInterval(updatePosition, 50);
            return () => { clearInterval(intervalId); };
        }, []);

        return [position, divRef];
    }
    const [position, ref] = useDivPosition(setTime);

    const nextSlide = () => {
        if(slideIndex !== images.length){
            setSlideIndex(slideIndex + 1);
        } else if (slideIndex === images.length){
            setSlideIndex(1);
        }
    }

    const prevSlide = () => {
        if(slideIndex !== 1){
            setSlideIndex(slideIndex - 1);
        } else if (slideIndex === 1) {
            setSlideIndex(images.length);
        }
    }


    const imageStyle = {
      width: 'auto',
      height: 'auto',
      minWidth: '100%',
      minHeight: '100%',
      transform: `translate(${-position.x}px, ${-position.y}px)`,
    };
    const sliderStyle = {
      width: width,
      height: height,
      overflow: 'hidden',
      position: 'relative',
    };
    if(((currentTimeInMs - screenEdgeTimeoutInMs) > 0) &&
      (1 - Math.cos(currentTimeInMs / 100000)) < .00001
    ) {
        const twentySecondsInMs = 20 * 1000;
        setTimeout(currentTimeInMs + twentySecondsInMs);
        nextSlide();
    }
    console.log('Render Slider %s', Math.abs(Math.cos(currentTimeInMs / 100000)));

    return (
      <div style={sliderStyle} ref={ref}>
        <img src={images[slideIndex - 1]} alt='Image' style={imageStyle} />
        <DriverStatsTicker title={title} />
      </div>
    );
};
export function mapStateToProps(state)
{
    return { };
}

export function mapDispatchToProps(dispatch)
{
   return{ };
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Slider));
