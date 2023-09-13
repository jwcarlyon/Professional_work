import {combineReducers} from 'redux';
import {driversReducer} from '../drivers/driversReducer';
import {lastAction} from './lastAction';

export default combineReducers({
    drivers: driversReducer
});
