"""
This file performs the following tasks:

1. Tokenize the given piece of text (based on a news article, opinion piece, column etc.)
into sentences.

2. Use NLTK's VADER SentimentIntensityAnalyzer to assess the polarity of each sentence.

3. Calculating the overall sentiment of the article by averaging the score assigned to each
sentence.
"""
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv


def read_csv(file_path: str) -> dict:
    """Open and read a CSV file into a Python dictionary."""
    csv_file = None
    with open(file_path, mode ='r')as file: 
        csv_file = csv.reader(file) 
        for lines in csv_file: 
            print(lines)


def read_text_file(file_path: str) -> str:
    """Open and read a .txt file into a String object."""
    article = []
    with open(file_path) as f:
        article = f.readlines()
    
    return article


def calculate_polarity(text: str) -> float:
    """Given a piece of text, calculate the sum total of the polarity of
    each sentence comprising the text, and return the mean."""
    tokens = sent_tokenize(text)
    sum_so_far = 0

    for token in tokens:
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(token)
        sum_so_far += scores['compound']  # Compound score reprsentes overall polarity of sentebce,
    
    return sum_so_far / len(tokens)

read_csv("../data/dataset.csv")


    
