import os
import subprocess
from string import punctuation
from nltk.corpus import stopwords
from collections import defaultdict


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


def download_data():
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "download_data.sh")
    subprocess.call([script_path], shell=True)


def fix(feature):
    feature = list(feature)
    feature[1] = strip_punctuation(feature[1]).lower()
    if len(feature) < 3:
        feature.append(0)
        return feature
    if feature[0] == "neg":
        feature[2] = 1 - feature[2]
    feature = tuple(feature)
    return feature


def monkey_patch_most_informative_features(self, n=100):
    features = set()
    maxprob = defaultdict(lambda: 0.0)
    minprob = defaultdict(lambda: 1.0)

    for (label, fname), probdist in self._feature_probdist.items():
        for fval in probdist.samples():
            p = probdist.prob(fval)
            feature = (label, fname, p)

            features.add(feature)

            maxprob[feature[2]] = max(p, maxprob[feature[2]])
            minprob[feature[2]] = min(p, minprob[feature[2]])
            if minprob[feature[2]] == 0:
                features.discard(feature)

    features = sorted(features,
                      key=lambda feature_:
                      minprob[feature_[2]] / maxprob[feature_[2]])

    return [fix(feature) for feature in features[:n]]


def strip_punctuation(s):
    return ''.join(c for c in s if ((c not in punctuation) or (c.isalnum())))
