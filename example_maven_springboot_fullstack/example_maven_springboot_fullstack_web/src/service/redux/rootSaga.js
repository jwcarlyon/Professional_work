import { all } from 'redux-saga/effects';
import * as driversSaga from '../drivers/driversSaga';

export default function * rootSaga() {
    yield all([
      driversSaga.watchGetDriverStats()
    ]);
}
