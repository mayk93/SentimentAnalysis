/**
 * Created by michael on 15/04/2017.
 */


import React from 'react';
import {Component} from 'react';


export default class App extends Component {
    constructor(props) {

        super(props);
    }

    render() {
        return (
            <div className="jumbotron small-jumbotron">
                <div className="page-header">
                  <h1>Sentiment Classifier <small>Built using</small></h1>
                </div>
                <hr/>
                <div className="block-container">
                    <div className="block">
                        <a href="https://www.djangoproject.com/">
                            <img className="tech-icon-small" src="images/django_logo.png"/>
                        </a>
                    </div>
                    <div className="block">
                        <a href="http://www.nltk.org/">
                            <img className="tech-icon" src="images/nltk_logo.png"/>
                        </a>
                    </div>
                    <div className="block">
                        <a href="https://facebook.github.io/react/">
                            <img className="tech-icon" src="images/react_logo.png"/>
                        </a>
                    </div>
                </div>
            </div>
        );
    }
}