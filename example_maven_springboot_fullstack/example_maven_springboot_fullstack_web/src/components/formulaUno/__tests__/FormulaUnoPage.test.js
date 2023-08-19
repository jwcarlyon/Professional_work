import regeneratorRuntime from 'regenerator-runtime';
import React from 'react';
import { render, screen } from '@testing-library/react';
import { createStore } from 'redux';

import { FormulaUnoPage } from '../FormulaUnoPage';
import rootReducer from '../../../service/redux/rootReducer';


jest.mock('../Slider', () => {
    return () => {
        return <div>Image Slider Backdrop Loaded</div>;
    };
});

describe('FormulaUnoPage', () => {
    beforeEach(() => {
        const initialState = { };
        const store = createStore(rootReducer, initialState);
        const mockDispatch = jest.fn();
        store.dispatch = mockDispatch;
        render
        (
          <FormulaUnoPage/>,
          { store: store }
        );
    });
    it('renders learn react link', () => {
        const linkElement = screen.getByText('Image Slider Backdrop Loaded');
        expect(linkElement).toBeInTheDocument();
    });
});
