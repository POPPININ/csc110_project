"""
This file contains helper functions which perform the following tasks:

1. Reading processed CSV data and,

2. Tokenizing a given article and gauging overall sentiment (by averaging the polarity of each sentence in
the article).
"""
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def calculate_average_polarity(text: str) -> float:
    """Given a piece of text, tokenize the text into sentences and compute the
    mean polarity of each sentence."""
    tokens = sent_tokenize(text)
    sum_so_far = 0

    for token in tokens:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(token)
        sum_so_far += scores['compound']  # Compound score reprsentes overall polarity of sentence,

    return sum_so_far / len(tokens)  # Return the average polarity of a sentence (thus the article)
