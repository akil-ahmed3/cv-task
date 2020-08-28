import json
import pdftotext
import pandas as pd

# nltk.download('punkt')
import os

from sklearn.feature_extraction.text import (
    TfidfTransformer,
    TfidfVectorizer,
    CountVectorizer,
)
import io
from collections import Counter

import numpy as np


def frequentAndEssentialWords(text):

    newText = text.split(",")

    tfIdfVectorizer = TfidfVectorizer(use_idf=True, stop_words="english")
    tfIdf = tfIdfVectorizer.fit_transform(newText)
    df = pd.DataFrame(
        tfIdf[0].T.todense(),
        index=tfIdfVectorizer.get_feature_names(),
        columns=["TF-IDF"],
    )
    df = df.sort_values("TF-IDF", ascending=False)
    tf = df.head(5)

    ngram_vectorizer = CountVectorizer(
        analyzer="word", ngram_range=(1, 1), min_df=1, stop_words="english"
    )
    X = ngram_vectorizer.fit_transform(newText)
    vocab = ngram_vectorizer.get_feature_names()
    counts = X.sum(axis=0).A1
    freq_distribution = Counter(dict(zip(vocab, counts)))
    frequent = pd.DataFrame(freq_distribution.most_common(10))

    return tf, frequent
