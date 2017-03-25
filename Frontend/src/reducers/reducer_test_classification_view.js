/**
 * Created by michael on 25/03/2017.
 */


export default function (state = {}, action) {
    switch (action.type) {
        case "TEST_CLASSIFICATION_RESULT":
            return action.payload;
        default:
            return state;
    }
}
