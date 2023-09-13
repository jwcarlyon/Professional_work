import { call, put, takeEvery } from '@redux-saga/core/effects';

import apiClient from '../apiClient/apiClient';
import * as driversActionTypes from './driversActionTypes';
import * as driversActionCreators from './driversActionCreators';

export function* watchGetDriverStats() {
    yield takeEvery(driversActionTypes.DRIVERS__GET_STATS, getDriverStats);
    setTimeout(function(){ return; }, 500);
}

export function* getDriverStats(action) {
  // try {
    const response = yield call(apiClient.get, `/drivers/${action.driverName}`);
    yield put(driversActionCreators.updateStats(response.data));
}
