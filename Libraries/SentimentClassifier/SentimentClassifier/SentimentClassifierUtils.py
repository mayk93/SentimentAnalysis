import os
from nltk.corpus import stopwords


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
