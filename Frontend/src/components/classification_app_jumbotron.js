/**
 * Created by michael on 15/04/2017.
 */


import React from 'react';
import {Component} from 'react';


export default class App extends Component {
    constructor(props) {
        super(props);

        this.image_number_to_position_normal = {
            0: "block link-class tech-icon-left",
            1: "block link-class",
            2: "block link-class tech-icon-right"
        };

        this.image_number_to_position_animate_left = {
            0: "hidden",
            1: "block link-class",
            2: "block link-class tech-icon-right"
        };

        this.image_number_to_position_animate_right = {
            0: "block link-class tech-icon-left",
            1: "block link-class",
            2: "hidden"
        };

        this.image_to_class = {
            0: "tech-icon",
            1: "tech-icon-small",
            2: "tech-icon",
            3: "tech-icon"
        };

        this.state = {
            images: [
                ["python", "https://www.python.org/", "images/python_logo.png"],
                ["django", "https://www.djangoproject.com/", "images/django_logo.png"],
                ["nltk", "http://www.nltk.org/", "images/nltk_logo.png"],
                ["react", "https://facebook.github.io/react/", "images/react_logo.png"]
            ],

            image_number_to_position: this.image_number_to_position_normal,

            shown_images: [0, 1, 2],
            offset: 0,
            timer_id: null
        };

        this.animate_left.bind(this);
        this.animate_right.bind(this);
        this.handle_left_click.bind(this);
        this.handle_right_click.bind(this);
        this.get_images(this);
    }

    animate_left() {
        if (this.state.offset == -150) {
            clearInterval(this.state.timer_id);
            this.setState({
                image_number_to_position: this.image_number_to_position_normal,
                shown_images: this.state.shown_images.map((value) => {
                    return (value + 1) % this.state.images.length;
                }),
                offset: 0
            });
        } else {
            this.setState({
               offset: this.state.offset - 5
            });
        }
    }

    animate_right() {
        if (this.state.offset == 150) {
            clearInterval(this.state.timer_id);
            this.setState({
                image_number_to_position: this.image_number_to_position_normal,
                shown_images: this.state.shown_images.map((value) => {
                    return (value - 1 + this.state.images.length) % this.state.images.length;
                }),
                offset: 0
            });
        } else {
            this.setState({
               offset: this.state.offset + 5
            });
        }
    }

    handle_left_click () {
        // ToDo: This is code duplication - Fix this
        this.setState({
            image_number_to_position: this.image_number_to_position_animate_left
        }, () => {
            this.setState({
                timer_id: setInterval(this.animate_left.bind(this), 10)
            });
        });
    }

    handle_right_click () {
        // ToDo: This is code duplication - Fix this
        this.setState({
            image_number_to_position: this.image_number_to_position_animate_right
        }, () => {
            this.setState({
                timer_id: setInterval(this.animate_right.bind(this), 10)
            });
        });
    }

    get_images() {
        let image_position;
        let image_href;
        let image_class;
        let image_source;

        return this.state.shown_images.map((image_number, index) => {
            image_position = this.state.image_number_to_position[index];
            image_href = this.state.images[image_number][1];
            image_class = index == 1 ? "tech-icon-middle" : this.image_to_class[image_number];
            image_source = this.state.images[image_number][2];
            return (
                <div key={image_number.toString() + "_" + index.toString()}
                     className={image_position}
                     style={{"transform": "translate3d(" + this.state.offset + "px, 0px, 0px)"}}
                >
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