import {combineReducers} from 'redux';

import TestViewReducer from './reducer_test_view';
import TestClassificationViewReducer from './reducer_test_classification_view';

const rootReducer = combineReducers({
    test_view_data: TestViewReducer,
    test_classification_view_data: TestClassificationViewReducer
});

export default rootReducer;

