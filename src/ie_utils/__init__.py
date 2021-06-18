# import pandas as pd

"""
IE Titanic utils.
"""

__version__ = "0.1.0"

import pandas as pd


def tokenize(text, lower=False, remove_stopwords=False, remove_punctuation=False):
    if lower:
        text=text.lower()
    if remove_stopwords:
        stopwords = ["a", "the", "or", "and"]
        words= text.split()
        non_stopwords = [w for w in words if not w.lower() in stopwords]
        text = " ".join(non_stopwords)             
    if remove_punctuation:
        punctuation = [".", ",", "!"]
        for p in punctuation:
            text = text.replace(p, '')
    return text.split()


if __name__ == "__main__":
    print(tokenize("Hello World!"))
