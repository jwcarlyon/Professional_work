import regeneratorRuntime from 'regenerator-runtime';
import React from 'react';
import {createRoot} from 'react-dom/client';
import {render, screen} from '@testing-library/react';
import {createStore} from 'redux';
import {Provider} from 'react-redux';

import App from '../App';
import rootReducer from '../../service/redux/rootReducer';

jest.mock('../debug/ReactPage', () => {
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
      const linkElement = screen.getByText('Loaded');
      expect(linkElement).toBeInTheDocument();
  });

});
