import React, { Component } from 'react';
import {connect} from 'react-redux';
import { Carousel } from 'react-bootstrap';

import Slider from './Slider';
import withRouter from '../utils/routerWrapper';
import '../../styles/FormulaUnoPage.css';

export class FormulaUnoPage extends Component
{
    constructor(props)
    {
        super(props);
        this.state =
        {
            date: new Date(),
            index: 0
        };
    }

    componentDidMount()
    {};

    formatDate = (date) => {
        const options = { day: '2-digit', month: 'short', year: 'numeric' };
        const formattedDate = date.toLocaleString('en-US', options);
        const [month, day, year] = formattedDate.split(' ');
        const capitalizedMonth = month.toUpperCase();

        return `${year}`;
    };
    //
    // handleNext = () => {
    //     console.log('handle next called.');
    //     const index = this.state.index;
    //     if(index >= 2){
    //         this.setState({ index: 0 });
    //     } else {
    //         this.setState({ index: this.state.index + 1 });
    //     }
    // };
    //
    renderTitle = () => {
        const titleText = 'Formula One Database ' + this.formatDate(this.state.date);
        return titleText;
    };


    render()
    {
        const nextSlide = () => {
            if(slideIndex !== dataSlider.length){
                setSlideIndex(slideIndex + 1);
            } else if (slideIndex === dataSlider.length){
                setSlideIndex(1);
            }
        }

        const prevSlide = () => {
            if(slideIndex !== 1){
                setSlideIndex(slideIndex - 1);
            } else if (slideIndex === 1){
                setSlideIndex(dataSlider.length);
            }
        }

        return (
          <Slider title={this.renderTitle}/>
        );
    }
}
// <Slider title={this.renderTitle}/>

    // <ReactSlider
    //   className='slideshow'
    //   trackClassName='track'
    //   thumbClassName='thumb'
    // >
    //   {images.map((image, i) => (
    //     <Slide
    //       key={i}
    //       image={image}
    //       title={this.renderTitle}
    //     />
    //   ))}
    // </ReactSlider>
// <div className='top-div'>
// <div className='floating-title'>
//   <h1>{titleText}</h1>
//   <h1 className='shadow'>{titleText}</h1>
// </div>
// <div className='carousel-div'>
//   <Carousel className='image-div'>
//     <Carousel.Item>
//       <img src={images[this.state.index]} onClick={this.handleNext}/>
//     </Carousel.Item>
//   </Carousel>
// </div>
// </div>
export function mapStateToProps(state)
{
    return { };
}

export function mapDispatchToProps(dispatch)
{
   return{
   };
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(FormulaUnoPage));
