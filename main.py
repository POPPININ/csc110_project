"""Add docstring."""
from article import Articles

articles = Articles()
articles.read_file('./dataset2.csv')
articles.run_sentiment()
