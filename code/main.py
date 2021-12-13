"""
This file performs the following tasks:

1. Use the NewsPlease library's web crawler to collect news articles and opinion pieces 
using their URLs from links.txt, process the data crawled, and dump it into a CSV file 
called 'dataset.csv'.

2. Represent each news article and opinion piece as an Article object, which can be collectively 
accessed through an Articles object via a mapping. We perform sentiment analysis on each Article's text
using NLTK, and assign the sentiment score to the Article's 'average_sentence_polarity' attribute.

3. Filter and classify the articles based on the themes discussed (e.g. Vaccine passport, travel bubbles,
Federal COVID-19 policies etc.), sort articles belonging to each theme by date published, and presenting
our findings using Plotly.
"""
from create_dataset import create_dataset
from csv_read_write import read_file
from article_classes import Article, Articles

# creates the dataset including web scraping, cleaning, sentiment analysis, etc. Will take a
# VERY long time to run. Approximately 5 minutes.
# Only uncomment if you need to recreate the dataset.
# create_dataset(
#     links_path='../data/links.text', 
#     dataset_save_path='../data/dataset.csv'
# )

# load the csv file
articles = read_file('../data/dataset.csv')
print(articles._articles)

# put code here to run graphing files