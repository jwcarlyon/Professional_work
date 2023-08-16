import {createStore, applyMiddleware} from 'redux';
import regeneratorRuntime from 'regenerator-runtime';
import createSagaMiddleware from 'redux-saga';

import rootReducer from '../../service/redux/rootReducer';
import rootSaga from '../../service/redux/rootSaga';

const sagaMiddleware = createSagaMiddleware(regeneratorRuntime);
const store = createStore(rootReducer, applyMiddleware(sagaMiddleware));
sagaMiddleware.run(rootSaga);

export default store;
