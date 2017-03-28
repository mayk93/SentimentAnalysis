import request from 'superagent';
import _ from 'lodash';


function test_view_post_liaison(data) {
    return {
        type: "TEST_VIEW_RESULT",
        payload: data
    };
}


export function test_view_post(data) {
    console.log("Sending ", data, " to test view.");
    return function(dispatch) {
        let test_request = request.post('/test_view/');
        test_request.send({"sent": data});
        test_request.end((error, response) => {
            if (error == null) {
                console.log("Success, made a POST to the test_view: ", response);
                dispatch(test_view_post_liaison(response.body.received));
            } else {
                console.log("Failed, did not make a POST to the test_view: ", error);
                return {
                    type: "TEST_VIEW_RESULT",
                    payload: "ERROR"
                };
            }
        });
    }
}

/* ----- */


function test_classification_liaison(data) {
    return {
        type: "TEST_CLASSIFICATION_RESULT",
        payload: data
    };
}


function _test_classification(dispatch, text) {
    let test_request = request.post('/test_classification/');
    test_request.send({"text": text});
    test_request.end((error, response) => {
        if (error == null) {
            dispatch(test_classification_liaison(response.body));
        } else {
            dispatch({
                type: "TEST_CLASSIFICATION_RESULT",
                payload: {}
            });
        }
    });
}

const debounced_test_classification = _.debounce((dispatch, text) => { _test_classification(dispatch, text)}, 250);

export function test_classification(text) {
    return (dispatch) => {
        debounced_test_classification(dispatch, text);
    }
}