/**
 * Created by michael on 28/03/2017.
 */


import React, {Component} from 'react';



export function list_to_li(word_list) {
    if (word_list == null || typeof word_list == "undefined") {
        return [];
    }
    return word_list.map((word) => {
        console.log(word);
        return <li key={word[0]}>{word[0]}</li>
    })
}
