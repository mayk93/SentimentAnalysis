import request from 'superagent';


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
        test_request.send(data);
        test_request.end((error, response) => {
            if (error == null) {
                console.log("Success, made a POST to the test_view: ", response);
                dispatch(test_view_post_liaison(response.body.data.received));
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