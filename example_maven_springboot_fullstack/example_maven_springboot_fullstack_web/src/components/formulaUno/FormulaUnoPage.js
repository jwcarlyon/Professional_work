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
export function mapStateToProps(state)
{
    return { };
}

export function mapDispatchToProps(dispatch)
{
   return{ };
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(FormulaUnoPage));
