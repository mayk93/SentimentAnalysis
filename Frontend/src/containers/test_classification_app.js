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

class TestClassificationApp extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: ""
        };
    }

    render() {
        return (
            <div>
                <textarea className="basic_text_area"
                          onChange={(event) => {this.setState({value: event.target.value})}} />
                <br/>
                <button onClick={() => {this.props.test_classification(this.state.value)}}>Send</button>
                <br/>
                <p>Result sentiment: {this.props.test_classification_view_data.sentiment}</p>
                <p>Result sentiment: {this.props.test_classification_view_data.confidence}</p>
                <p>Result sentiment: {this.props.test_classification_view_data.classification_words}</p>
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
