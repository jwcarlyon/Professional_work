import regeneratorRuntime from 'regenerator-runtime';
import React from 'react';
import {createRoot} from 'react-dom/client';
import {render, screen} from '@testing-library/react';
import {createStore} from 'redux';
import {Provider} from 'react-redux';

import App from '../App';
import rootReducer from '../../service/redux/rootReducer';

jest.mock('../formulaUno/FormulaUnoPage', () => {
    return () => {
        return <div>Welcome Page Loaded</div>;
    };
});

describe('App', () => {
    beforeEach(() => {
        const initialState = { ui: ''};
        const store = createStore(rootReducer, initialState);
        const mockDispatch = jest.fn();
        store.dispatch = mockDispatch;
        render
        (
          <Provider store={store}>
            <App />
          </Provider>
        );
    });

  it('renders learn react link', () => {
      const linkElement = screen.getByText('Welcome Page Loaded');
      expect(linkElement).toBeInTheDocument();
  });

});
