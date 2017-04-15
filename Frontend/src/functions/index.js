/**
 * Created by michael on 28/03/2017.
 */


import React, {Component} from 'react';


// Find a way to made more general
export function list_to_li(word_list) {
    if (word_list == null || typeof word_list == "undefined") {
        return [];
    }
    return word_list.map((word) => {

        let class_name = "label ";
        class_name += (word[0] == "pos" ? "blue" : "red");
        class_name += "-" + (word[2] > 0.5 ? "strong" : "weak");

        return (
            <li key={word[1]} className="list-group-item ">
                <span className={class_name}>{word[1]}</span>
            </li>
        );
    })
}
