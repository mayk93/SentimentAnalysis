import React from 'react';
import {Component} from 'react';

// import TestViewApp from '../containers/test_view_app';
import TestClassificationApp from '../containers/test_classification_app';

export default class App extends Component {
    constructor(props) {

        super(props);
    }

    render() {
        return (
            <div>
                <br/>
                <div className="jumbotron small-jumbotron">
                    <h1>Sentiment classifier</h1>
                    <hr/>
                    <div className="block-container">
                        <div className="block">
                            <img className="tech-icon-90" src="images/django_logo.png"/>
                        </div>
                        <div className="block">
                          <img className="tech-icon" src="images/nltk_logo.png"/>
                        </div>
                        <div className="block">
                          <img className="tech-icon" src="images/react_logo.png"/>
                        </div>
                    </div>
                </div>
                <TestClassificationApp />
                <hr/>
                <h3>
                    Hosted on
                    <span className="span-padding-left">
                    <i className="fa fa-github" aria-hidden="true">

                    </i>
                    </span>
                </h3>
            </div>
        );
    }
}
