import React, { Component } from 'react';
import {connect} from 'react-redux';

import driverPhoto from'../../styles/visualAssets/theStig.jpg';
import withRouter from '../utils/routerWrapper';
import '../../styles/DriverStatsTicker.css';

export class DriverStatsTicker extends Component
{
    constructor(props)
    {
        super(props);
        this.state = {  };
    }

    componentDidMount()
    {};

    render()
    {
        return (
          <div className='floating-window'>
            <div className='driver-photo'>
              <img src={driverPhoto} alt='Photo' className='photo' />
            </div>
            <div className='bio-table'>
              <p className='bio-text'>
                Some say he can smell carbon emissions, and that he once drove a Bugatti Veyron backwards around the Nürburgring.
                <br/>Some say he has a third eye on the back of his head, and that he only eats gravel.
                <br/>Some say he can speak fluent Klingon, and that he has a pet velociraptor.
                <br/>Some say he is immune to gravity, and that he invented the wheel.
                <br/>Some say he is a secret agent, and that he once killed a man with a banana.
                <br/>Some say he is allergic to sunlight, and that he has a tattoo of Jeremy Clarkson on his chest.
                <br/>Some say he is a master of disguise, and that he once impersonated the Queen.
                <br/>Some say he is a time traveler, and that he was the first man on the moon.
                <br/>Some say he is a vampire, and that he sleeps in a coffin filled with oil.
                <br/>Some say he is a wizard, and that he can turn water into petrol.
                <br/>All we know is he’s called the Stig.
              </p>
            </div>
          </div>
        );
    };
};

export function mapStateToProps(state)
{
    return{ };
}

export function mapDispatchToProps(dispatch)
{
   return{ };
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(DriverStatsTicker));
