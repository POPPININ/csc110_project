"""
Tokenizing a given article and gauging overall sentiment (by averaging the polarity of
each sentence in the article). Implementation leverages the NLTK library, and a modified
version of the VADER analysis tool.


Copyright and Usage Information
===============================
Code by Raghav Arora, December 2021


------------------------------------
Copyright (C) 2001-2021 NLTK Project
------------------------------------
Author: C.J. Hutto <Clayton.Hutto@gtri.gatech.edu>
        Ewan Klein <ewan@inf.ed.ac.uk> (modifications)
        Pierpaolo Pantone <24alsecondo@gmail.com> (modifications)
        George Berry <geb97@cornell.edu> (modifications)
        Malavika Suresh <malavika.suresh0794@gmail.com> (modifications)
URL: <https://www.nltk.org/>

------------------------
VADER Sentiment Analyzer
------------------------

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
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


if __name__ == '__main__':
    import python_ta
    import doctest
    import python_ta.contracts

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': ['python_ta.contracts', 'nltk.tokenize', 'nltk.sentiment.vader'],
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200']
    })
