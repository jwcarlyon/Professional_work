import React, {Component} from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import {connect} from 'react-redux';

import DebugPage from './debug/DebugPage';
import FormulaUnoPage from './formulaUno/FormulaUnoPage';


class App extends Component
{
    render()
    {
        return(
          <React.StrictMode>
            <BrowserRouter>
              <Routes>
                <Route exact path="/" element={<FormulaUnoPage />} />
                <Route exact path="/debug" element={<DebugPage />} />
              </Routes>
            </BrowserRouter>
          </React.StrictMode>
        );
    }
}

export function mapStateToProps(state)
{
    return {};
}

export default connect(mapStateToProps, {})(App);
