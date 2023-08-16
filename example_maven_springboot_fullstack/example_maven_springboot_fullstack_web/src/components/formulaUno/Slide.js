import React, {Component} from 'react';
import {connect} from 'react-redux';

import '../../styles/FormulaUnoPage.css';
import withRouter from '../utils/routerWrapper';

export class Slide extends Component
{
  constructor(props)
  {
      super(props);
      this.state = {};
  }

  componentDidMount()
  {};

  render()
  {
      console.log('render Slide: %s', this.props.image);
      const imageStyle = 'background-image: ' + this.props.image;
      return (
        <div className='slide' style={imageStyle}>
          <h1 className='title'>{this.props.title}</h1>
        </div>
      );
  };
}

export function mapStateToProps(state)
{
    return{ };
}

export function mapDispatchToProps(dispatch)
{
   return{ };
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Slide));
