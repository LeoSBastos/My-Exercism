"""
Counting words
"""

from string import punctuation

import re


def count_words(sentence):
    """
    Remove punctuation and add to a dictionary
    """

    result = dict()
    my_punctuation = punctuation.replace("'", "")
    puncless = sentence.translate(str.maketrans(
        my_punctuation, " "*len(my_punctuation)))
    puncless = re.sub(
        r"(?<![A-Za-z])'+(?=[A-Za-z])|(?<=[.A-Za-z])'+(?![A-Za-z])", " ", puncless)
    wordlist = set(puncless.split())
    result = {word.lower(): puncless.lower().split().count(word.lower())
              for word in wordlist}
    return result
