import React from 'react';
import {Component} from 'react';

import TestViewApp from '../containers/test_view_app';

export default class App extends Component {
    constructor(props) {

        super(props);
    }

    render() {
        return (
            <div>
                <TestViewApp />
            </div>
        );
    }
}
