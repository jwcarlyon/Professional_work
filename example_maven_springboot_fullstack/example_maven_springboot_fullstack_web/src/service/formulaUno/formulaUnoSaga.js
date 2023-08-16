import { takeEvery } from '@redux-saga/core/effects';

import * as formulaUnoActionTypes from './formulaUnoActionTypes';
import * as formulaUnoActionCreators from './formulaUnoActionCreators';

export function* watchNext() {
    // yield takeEvery(formulaUnoActionTypes.CAROUSEL__NEXT, next);
}

export function* watchPrev() {
    // yield takeEvery(formulaUnoActionTypes.CAROUSEL__PREV, prev);
}
