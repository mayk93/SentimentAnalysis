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

/* Other Components */
import Textarea from 'react-textarea-autosize';

class TestClassificationApp extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: ""
        };

        this.handle_text_area_change.bind(this);

    }

    handle_text_area_change(event) {
        this.setState({value: event.target.value}, () => {
            this.props.test_classification(this.state.value);
        });
    }

    render() {
        return (
            <div>
                <Textarea className="basic_text_area"
                          onChange={(event) => {this.handle_text_area_change(event)}} />
                <br/>
                <button onClick={() => {this.props.test_classification(this.state.value)}}>Send</button>
                <br/>
                <p>Result sentiment: {this.props.test_classification_view_data.sentiment}</p>
                <p>Result confidence: {this.props.test_classification_view_data.confidence}</p>
                <p>Result classification words : {this.props.test_classification_view_data.classification_words}</p>
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
