
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
    version='0.0.73',

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

