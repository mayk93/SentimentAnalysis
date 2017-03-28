/**
 * Created by michael on 25/03/2017.
 */

/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import { test_classification } from '../actions/index';

/* Other */
import { list_to_li } from '../functions/index';

class TestClassificationApp extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: "",
            // key_number: 0
        };

        this.handle_text_area_change.bind(this);
        list_to_li.bind(this);
    }

    handle_text_area_change(event) {
        this.setState({value: event.target.value}, () => {
            this.props.test_classification(this.state.value);
        });
    }

    render() {
        return (
            <div>
                <form style={{"padding": "10px"}}>
                    <textarea className="form-control basic_text_area"
                              onChange={(event) => {this.handle_text_area_change(event)}} />
                </form>

                <hr/>

                <p className="result_sentiment">
                    Result sentiment: {this.props.test_classification_view_data.sentiment}
                </p>
                <p className="result_confidence">
                    Result confidence: {this.props.test_classification_view_data.confidence}
                </p>
                <p className="confidence_color" style={{"backgroundColor": "red"}}>

                </p>

                <hr/>

                <p>Result classification words :</p>
                <ul>
                    {list_to_li(this.props.test_classification_view_data.classification_words)}
                </ul>
            </div>
        )

    }
}

function mapStateToProps(state) {
    return {
      test_classification_view_data: state.test_classification_view_data
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators({ test_classification }, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(TestClassificationApp);
