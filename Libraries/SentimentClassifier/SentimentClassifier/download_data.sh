#!/usr/bin/env bash

CURRENT_DIRECTORY=$(pwd)

cd /tmp/

mkdir sentiment_data

cd sentiment_data

/usr/local/bin/wget https://archive.ics.uci.edu/ml/machine-learning-databases/00331/sentiment%20labelled%20sentences.zip

unzip sentiment\ labelled\ sentences.zip

mv sentiment\ labelled\ sentences sentiment_labelled_sentences

cd $CURRENT_DIRECTORY