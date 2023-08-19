import regeneratorRuntime from 'regenerator-runtime';
import React from 'react';
import { render, screen } from '@testing-library/react';
import { createStore } from 'redux';

import { Slider } from '../Slider';
import rootReducer from '../../../service/redux/rootReducer';

jest.mock('../../drivers/DriverStatsTicker', () => {
    return () => {
        return <div>DriverStatsTicker Loaded</div>;
    };
});

describe('Slider', () => {
    beforeEach(() => {
        const store = createStore(rootReducer, {});
        const mockDispatch = jest.fn();
        store.dispatch = mockDispatch;
        const titleText = jest.fn();
        render(<Slider props={titleText} store={store}/>);
    });

    it('renders learn react link', () => {
        const linkElement = screen.getByText('DriverStatsTicker Loaded');
        expect(linkElement).toBeInTheDocument();
    });
});
