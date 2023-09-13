import React, { Component } from 'react';
import {connect} from 'react-redux';

import { getDriverStats } from '../../service/drivers/driversActionCreators';
import driverPhoto from '../../styles/visualAssets/theStig.jpg';
import withRouter from '../utils/routerWrapper';
import '../../styles/DriverStatsTicker.css';

export class DriverStatsTicker extends Component
{
    constructor(props)
    {
        super(props);
        this.state = { title: this.props.title };
    }

    componentDidMount()
    {
        const driverName = this.props.driverName ? this.props.driverName : 'Lewis';
        this.props.getDriverStats(driverName);
    }

    createBioPage = (stats) => {
        return(
          <div>
            <p>Driver ID: {stats.driverId}</p>
            <p>Car Number: {stats.permanentNumber}</p>
            <a href={stats.url}>Wikipedia Numbers</a>
            <p>Name: {stats.givenName} {stats.familyName}</p>
            <p>DOB: {stats.dateOfBirth}</p>
            <p>Nationality: {stats.nationality}</p>
          </div>
        );
    };

    renderStats = () => {
        if(this.props.stats) {
            return(this.createBioPage(this.props.stats));
        }
        return(
          this.state.title()
        );
    };

    render()
    {
        return (
          <div className='floating-window'>
            <div className='driver-photo'>
              <img src={driverPhoto} alt='Photo' className='photo' />
            </div>
            <div className='bio-table'>
              <p className='bio-text'>
                {this.renderStats()}
              </p>
            </div>
          </div>
        );
    }
}

export function mapStateToProps(state)
{
    if(state.drivers){
        return{
          stats: state.drivers.stats
        };
    }
    return {};
}

export function mapDispatchToProps(dispatch)
{
     return{
       getDriverStats: (driverName) => dispatch(getDriverStats(driverName))
     };
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(DriverStatsTicker));
