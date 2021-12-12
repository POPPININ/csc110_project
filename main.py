"""
do we need a docstring? probably

"""

from create_dataset import create_dataset
from csv_read_write import read_file
from article_classes import Article, Articles

# creates the dataset including web scraping, cleaning, sentiment analysis, etc. Will take a
# VERY long time to run. Approximately 5 minutes.
# Only uncomment if you need to recreate the dataset.
# create_dataset()

# load the csv file
articles = read_file('./dataset.csv')

# put code here to run graphing files
