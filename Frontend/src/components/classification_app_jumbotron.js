/**
 * Created by michael on 15/04/2017.
 */


import React from 'react';
import {Component} from 'react';


export default class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            // ToDo: Change to dictionary
            images: [
                ["django", "https://www.djangoproject.com/"],
                ["nltk", "http://www.nltk.org/"],
                ["react", "https://facebook.github.io/react/"]
            ],
            shown_images: [0, 1, 2]
        };

        this.handle_left_click.bind(this);
        this.handle_right_click.bind(this);
        this.get_images(this);
    }
    handle_left_click () {
        this.setState({
            shown_images: this.state.shown_images.map((value) => {
                return (value + 1) % this.state.images.length;
            })
        }, () => {console.log(this.state.shown_images)})
    }

    handle_right_click () {
        this.setState({
            shown_images: this.state.shown_images.map((value) => {
                return (value - 1 + this.state.images.length) % this.state.images.length;
            })
        }, () => {console.log(this.state.shown_images)})
    }

    get_images() {
        let image_position = "";  // tech-icon-left
        let image_source = ""; //
        let image_class = ""; // "tech-icon-small"

        return this.state.shown_images.map((image_number) => {
            return (
                <div className={"block " + image_position}>
                    <a href={image_source}>
                        <img className={image_class} src="images/django_logo.png"/>
                    </a>
                </div>
            );
        });

        /*

        <div className="block tech-icon-left">
            <a href="https://www.djangoproject.com/">
                <img className="tech-icon-small" src="images/django_logo.png"/>
            </a>
        </div>

        <div className="block">
            <a href=>
                <img className={image_class} src="images/nltk_logo.png"/>
            </a>
        </div>

        <div className="block tech-icon-right">
            <a href=>
                <img className="tech-icon" src="images/react_logo.png"/>
            </a>
        </div>

        */

        // // ToDo: Find a way to generalize this to multiple
        // // ToDo: That is, even if you have 5, show only 3 this way
        // return this.state.images.map((element, index) => {
        //         if (index < )
        // });
    }

    render() {
        let image_class = "tech-icon-middle";
        let images = this.get_images();

        return (
            <div className="jumbotron small-jumbotron">
                <div className="page-header">
                  <h1>Sentiment Classifier <small>Built using</small></h1>
                </div>
                <hr/>
                <div className="block-container">
                    <div className="block left">
                        <i className="fa fa-chevron-left center arrow-hover" aria-hidden="true"
                           onClick={() => {this.handle_left_click()}}></i>
                    </div>
                    {images}
                    <div className="block right">
                        <i className="fa fa-chevron-right center arrow-hover" aria-hidden="true"
                           onClick={() => {this.handle_right_click()}}></i>
                    </div>
                </div>
            </div>
        );
    }
}