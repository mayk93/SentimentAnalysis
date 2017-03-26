import nltk


class SentimentClassifier(object):
    def __init__(self):
        self.test_attribute = "SentimentClassifier works."

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
        self.assertEquals(self.sc.test_attribute, "SentimentClassifier works.")
        self.assertEquals(self.sc.classify({"text": "test"}), "SentimentClassifier works.")