/**
 * Created by michael on 15/04/2017.
 */


import React from 'react';
import {Component} from 'react';


export default class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            images: [
                ["python", "https://www.python.org/", "images/python_logo.png"],
                ["django", "https://www.djangoproject.com/", "images/django_logo.png"],
                ["nltk", "http://www.nltk.org/", "images/nltk_logo.png"],
                ["react", "https://facebook.github.io/react/", "images/react_logo.png"]
            ],
            shown_images: [0, 1, 2]
        };

        this.image_number_to_position = {
            0: " tech-icon-left",
            1: "",
            2: " tech-icon-right"
        };

        this.image_to_class = {
            0: "tech-icon",
            1: "tech-icon-small",
            2: "tech-icon",
            3: "tech-icon"
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
        let image_position;
        let image_href;
        let image_class;
        let image_source;

        return this.state.shown_images.map((image_number, index) => {
            image_position = this.image_number_to_position[index];
            image_href = this.state.images[image_number][1];
            image_class = index == 1 ? "tech-icon-middle" : this.image_to_class[image_number];
            image_source = this.state.images[image_number][2];
            return (
                <div key={image_number.toString() + "_" + index.toString()} className={
                    "block link_class " + image_position
                }>
                    <a href={image_href}>
                        <img className={image_class} src={image_source}/>
                    </a>
                </div>
            );
        });
    }

    render() {
        let images = this.get_images();

        return (
            <div className="jumbotron small-jumbotron">
                <div className="page-header">
                  <h1>Sentiment Classifier</h1>
                  <small>Built using</small>
                </div>
                <hr/>
                <div className="block-container">
                    <div className="block left">
                        <i className="fa fa-chevron-left center arrow-hover" aria-hidden="true"
                           onClick={() => {this.handle_left_click()}}>

                        </i>
                    </div>
                    {images}
                    <div className="block right">
                        <i className="fa fa-chevron-right center arrow-hover" aria-hidden="true"
                           onClick={() => {this.handle_right_click()}}>

                        </i>
                    </div>
                </div>
            </div>
        );
    }
}