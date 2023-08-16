import { all } from 'redux-saga/effects';
import * as formulaUnoSaga from '../formulaUno/formulaUnoSaga';

export default function * rootSaga() {
    yield all([
      formulaUnoSaga.watchNext(),
      formulaUnoSaga.watchPrev()
    ]);
}
