import React from 'react';
import {Component} from 'react';

import ClassificationApp from '../containers/classification_app';
import ClassificationAppJumbotron from '../components/classification_app_jumbotron';
import ClassificationAppFooter from '../components/classification_app_footer';


export default class App extends Component {
    constructor(props) {

        super(props);
    }

    render() {
        return (
            <div>
                <br/>
                <ClassificationAppJumbotron/>
                <ClassificationApp />
                <hr/>
                <ClassificationAppFooter/>
            </div>
        );
    }
}
