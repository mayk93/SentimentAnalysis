/**
 * Created by michael on 23/03/2017.
 */

/* React */
import React, {Component} from 'react';

/* Redux */
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

/* Actions */
import { test_view_post } from '../actions/index';

class TestViewApp extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: ""
        };
    }

    render() {
        return (
            <div>
                <input type="text" onChange={(event) => {this.setState({value: event.target.value})}} />
                <br/>
                <button onClick={() => {this.props.test_view_post(this.state.value)}}>Send</button>
                <br/>
                <p>You sent: {this.props.test_view_data}</p>
            </div>
        )

    }
}

function mapStateToProps(state) {
    return {
      test_view_data: state.test_view_data
    };
}

function mapDispatchToProps(dispatch) {
    return bindActionCreators({ test_view_post }, dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(TestViewApp);