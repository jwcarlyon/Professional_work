import React, {Component} from 'react';
import {connect} from 'react-redux';

import logo from '../../styles/logo.svg';
import '../../styles/DebugPage.css';
import withRouter from '../utils/routerWrapper';

export class DebugPage extends Component
{
    constructor(props)
    {
        super(props);
        this.state = { rotating: true };
    }

    componentDidMount()
    {};

    handleRotation = () =>
    {
        if(this.state.rotating === true)
        {
            this.setState({ rotating: false });
        } else {
            this.setState({ rotating: true });
        }
    };

    render()
    {
        return(
          <div>
            <div className="App">
              <header className="App-header">
                <img
                  src={logo}
                  className={(this.state.rotating ? "App-logo": " App-logo-paused")}
                  alt="logo"
                  onClick={this.handleRotation}
                />
                <p>
                  Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
              </header>
            </div>
          </div>
        );
    }
}

export function mapStateToProps(state)
{
    return {};
}

export function mapDispatchToProps(dispatch)
{
   return{};
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(DebugPage));
