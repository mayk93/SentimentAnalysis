#!/usr/bin/env bash

CURRENT_DIRECTORY=$(pwd)

echo "Starting from: $CURRENT_DIRECTORY"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

echo "Now in $DIR"

python increase_version.py

CURRENT_VERSION=$(cat current_version)

echo "Rebuilding with version $CURRENT_VERSION"

echo """
#!/usr/bin/env python

import sys

from setuptools import setup, find_packages
from codecs import open
from os import path

current_path = path.abspath(path.dirname(__file__))

with open(path.join(current_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SentimentClassifier',
    version='$CURRENT_VERSION',

    description='A library used in the Sentiment Analysis app',
    long_description=long_description,

    author='Michael',
    author_email='mihai@mandrescu.co',
    url='http://www.mandrescu.co',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],

    keywords='nltk',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={
          'SentimentClassifier': ['*.sh'],
    },
    install_requires=['nltk']
)
""" > setup.py

python setup.py bdist_wheel

cd dist

pwd
ls

echo "Installing SentimentClassifier-$CURRENT_VERSION-py2-none-any.whl"

pip install SentimentClassifier-$CURRENT_VERSION-py2-none-any.whl

cd ../../../SentimentAnalysis_env/lib/python2.7/site-packages/SentimentClassifier
chmod 744 download_data.sh

cd $CURRENT_DIRECTORY