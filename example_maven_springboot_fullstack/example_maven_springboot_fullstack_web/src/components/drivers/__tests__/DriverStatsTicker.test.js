import regeneratorRuntime from 'regenerator-runtime';
import React from 'react';
import { render, screen } from '@testing-library/react';
import { createStore } from 'redux';

import { DriverStatsTicker } from '../DriverStatsTicker';
import rootReducer from '../../../service/redux/rootReducer';

describe('DriverStatsTicker', () => {
    beforeEach(() => {
        const store = createStore(rootReducer, {});
        const mockDispatch = jest.fn();
        store.dispatch = mockDispatch;
        const titleText = jest.fn();
        render(<DriverStatsTicker props={titleText} store={store}/>);
    });

    it('renders learn react link', () => {
        const linkElement = screen.getByRole('img');
        expect(linkElement).toBeInTheDocument();
    });
});
