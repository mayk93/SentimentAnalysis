import os
import pickle
from string import punctuation

# NLTK #
# ==================================================================================================================== #

import collections
from nltk.classify import NaiveBayesClassifier

from SentimentClassifierUtils import get_data, remove_stopwords

# ==================================================================================================================== #


# Settings
# ==================================================================================================================== #

NUMBER_OF_WORDS = 500

# ==================================================================================================================== #


def monkey_patch_most_informative_features(self, n=100):
    from collections import defaultdict
    features = set()
    maxprob = defaultdict(lambda: 0.0)
    minprob = defaultdict(lambda: 1.0)

    for (label, fname), probdist in self._feature_probdist.items():
        for fval in probdist.samples():
            p = probdist.prob(fval)
            feature = (fname, p)

            features.add(feature)

            maxprob[feature] = max(p, maxprob[feature])
            minprob[feature] = min(p, minprob[feature])
            if minprob[feature] == 0:
                features.discard(feature)

    features = sorted(features,
                      key=lambda feature_:
                      minprob[feature_] / maxprob[feature_])
    return features[:n]


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


class SentimentClassifier(object):
    def __init__(self):
        self.classifier = None
        self.classifier_path = "/tmp/simple_sentiment_classifier"
        self.data_source = "/tmp/sentiment_data/sentiment_labelled_sentences"
        self.words = None

        if not os.path.exists(self.data_source) and not os.path.exists(self.classifier_path):
            raise Exception("No data set or classifier found. Please run the download_data script.")

    def get_classifier(self):
        # Try to load or train a new classifier
        try:
            self._load()
        except IOError:
            self._train()
            self._save()

        if self.classifier is None:
            raise Exception("Could not get classifier.")

    def _load(self):
        with open(self.classifier_path, 'rb') as source:
            self.classifier = pickle.load(source)
            self.classifier.most_informative_features = monkey_patch_most_informative_features
            self.words = self.classifier.most_informative_features(self.classifier, NUMBER_OF_WORDS)

    def _save(self):
        with open('simple_classifier.pickle', 'wb') as destination:
            pickle.dump(self.classifier, destination)

    def _train(self):
        self.data = get_data(self.data_source,
                             ["amazon_cells_labelled.txt",
                              "imdb_labelled.txt",
                              "yelp_labelled.txt"])

        negative_words = [(remove_stopwords(sentence.split()), 'neg') for sentence, label in self.data if label == 0]
        positive_words = [(remove_stopwords(sentence.split()), 'pos') for sentence, label in self.data if label == 1]

        negative_test_split = len(negative_words) * 3 / 4
        positive_test_split = len(positive_words) * 3 / 4

        train_words = negative_words[:negative_test_split] + positive_words[:positive_test_split]
        test_words = negative_words[negative_test_split:] + positive_words[positive_test_split:]

        classifier = NaiveBayesClassifier.train(train_words)
        correct_labels = collections.defaultdict(set)
        predictions = collections.defaultdict(set)

        for i, (feats, label) in enumerate(test_words):
            correct_labels[label].add(i)
            observed = classifier.classify(feats)
            predictions[observed].add(i)

        self.classifier = classifier
        self.classifier.most_informative_features = monkey_patch_most_informative_features
        self.words = self.classifier.most_informative_features(self.classifier, NUMBER_OF_WORDS)

    def classify(self, classification_input):
        text_words = classification_input.get("text", "").split(" ")
        classification_words = set()
        classification_input_dict = {}

        for word in text_words:
            classification_input_dict[word] = True

        result = self.classifier.classify(classification_input_dict)

        for classification_word, classification_value in self.words:
            if len(classification_word) > 3 and strip_punctuation(classification_word) in text_words:
                classification_words.add((classification_word, classification_value))

        classification_words = list(classification_words)
        print classification_words

        return {
            "sentiment": result,
            "confidence": 0,  # ToDo: Get classification confidence
            "classification_words": classification_words
        }


import unittest


class TestSentimentClassifier(unittest.TestCase):
    def setUp(self):
        self.sc = SentimentClassifier()

    def tearDown(self):
        del self.sc

    def test_SentimentClassifier(self):
        self.assertEquals(self.sc.classify({"text": "test"}), "SentimentClassifier works.")

    def test_get_data(self):
        result = get_data("/tmp/sentiment_data/sentiment_labelled_sentences",
                          ["amazon_cells_labelled.txt",
                           "imdb_labelled.txt",
                           "yelp_labelled.txt"])

        self.assertEquals(len(result), 3000)

        # Make sure there is 1500 0 labels and 1500 1 labels
        count_0 = 0
        count_1 = 0
        for _, label in result:
            if label == 0:
                count_0 += 1
            elif label == 1:
                count_1 += 1
            else:
                raise Exception("Unknown label found.")

        self.assertEquals(1500, count_0)
        self.assertEquals(1500, count_1)

    def test_train(self):
        self.sc._train()
        classification_input = {}
        for word in "Hello. This is a good thing. Happy!".split():
            classification_input[word] = True
        print self.sc.classifier.classify(classification_input)
        for word in "This sucks, it is horrible!".split():
            classification_input[word] = True
        print self.sc.classifier.classify(classification_input)