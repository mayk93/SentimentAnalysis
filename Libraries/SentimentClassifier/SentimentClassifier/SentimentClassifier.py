import os
import pickle

# NLTK #
# ==================================================================================================================== #

import collections
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier

from nltk import precision
from nltk import recall

from nltk.corpus import stopwords

# ==================================================================================================================== #


def get_data(path, files):
    data = []

    for file_name in files:
        with open(os.path.join(path, file_name)) as source:
            for line in source.readlines():
                sentence, label = line.split("\t")
                label = int(label)
                data.append((sentence, label))

    return data


def remove_stopwords(words):
    return dict([(word, True) for word in words if word not in stopwords.words("english")])


class SentimentClassifier(object):
    def __init__(self):
        self.classifier = None
        self.classifier_path = "/tmp/simple_sentiment_classifier"
        self.data_source = "/tmp/sentiment_data/sentiment_labelled_sentences"

        # At least one of these must exist
        # ToDo: Can this be made better?
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
            
        print 'accuracy:', nltk.classify.util.accuracy(classifier, test_words)
        print 'pos precision:', precision(correct_labels['pos'], predictions['pos'])
        print 'pos recall:', recall(correct_labels['pos'], predictions['pos'])
        print 'neg precision:', precision(correct_labels['neg'], predictions['neg'])
        print 'neg recall:', recall(correct_labels['neg'], predictions['neg'])
        classifier.show_most_informative_features(50)

        self.classifier = classifier

    def classify(self, classification_input):
        classification_input_dict = {}
        for word in classification_input.get("text", "").split(" "):
            classification_input_dict[word] = True

        result = self.classifier.classify(classification_input_dict)
        print result

        return {
            "sentiment": result,
            "confidence": 0,
            "classification_words": classification_input.get("text", "").split(" ")
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