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
            value: ""
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
        let sentiment = (this.props.test_classification_view_data.sentiment == "pos" ?
            "This is a positive sentiment!" : "This is a negative sentiment!");
        let confidence = this.props.test_classification_view_data.confidence;
        let classification_words = this.props.test_classification_view_data.classification_words;
        let result_sentiment_span = (this.props.test_classification_view_data.sentiment == "pos" ?
            "label blue-strong" : "label red-strong");

        // ToDo: Fix the styles
        return (
            <div>
                <form style={{"padding": "10px"}}>
                    <textarea className="form-control basic_text_area"
                              onChange={(event) => {this.handle_text_area_change(event)}} />
                </form>

                <hr/>

                <p className="result_sentiment">
                    Result sentiment: <span className={result_sentiment_span}>{sentiment}</span>
                </p>
                <p className="result_confidence">
                    Result confidence: {confidence}
                </p>
                <p className="confidence_color" style={{"backgroundColor": "red"}}>

                </p>

                <hr/>

                <p>Result classification words :</p>
                <ul className="list-group">
                    {list_to_li(classification_words)}
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
