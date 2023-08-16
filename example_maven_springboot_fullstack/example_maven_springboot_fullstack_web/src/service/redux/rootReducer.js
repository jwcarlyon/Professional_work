import {combineReducers} from 'redux';
import {formulaUnoReducer} from '../formulaUno/formulaUnoReducer';
import {uiReducer} from '../ui/uiReducer';

export default combineReducers
({
    f1Carosel: () => formulaUnoReducer,
    ui: () => uiReducer
});
