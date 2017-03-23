import {combineReducers} from 'redux';

import TestViewReducer from './reducer_test_view';

const rootReducer = combineReducers({
    test_view_data: TestViewReducer
});

export default rootReducer;

