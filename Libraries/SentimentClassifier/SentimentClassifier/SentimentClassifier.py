import os
import nltk
import pickle


def get_data(path, files):
    data = []

    for file_name in files:
        with open(os.path.join(path, file_name)) as source:
            for line in source.readlines():
                sentence, label = line.split("\t")
                label = int(label)
                data.append((sentence, label))

    return data


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
        with open('my_classifier.pickle', 'wb') as destination:
            pickle.dump(self.classifier, destination)

    def _train(self):
        self.data = get_data(self.data_source,
                             ["amazon_cells_labelled.txt",
                              "imdb_labelled.txt",
                              "yelp_labelled.txt"])

    def classify(self, classification_input):
        return {
            "sentiment": "Unknown",
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