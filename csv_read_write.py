"""
reads and writes to csv

Code by Anna and Raghav
"""
import csv
from article_classes import Article, Articles
from datetime import datetime


def read_file(file_path: str) -> Articles:
    """Read csv file and populate Articles object where each row in the csv is an item in
    _articles and corresponds to an Article object.
    """
    articles = Articles()
    with open(file_path, mode='r', encoding='UTF8') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            article = Article(
                title=row['title'],
                date_published=datetime.strptime(row['date_publish'], "%Y-%m-%d %H:%M:%S"),
                authors=row['authors'],
                main_text=row['maintext'],
                source_domain=row['source_domain'],
                url=row['url'],
                average_sentence_polarity=row['average_sentence_polarity'],
                description=row['description']
            )
            articles.add_article(article)

    return articles


def write_file(a: Articles) -> None:
    """ Create a csv file containing all the cleaned data from the web scraping.
    """
    # open the file in the write mode
    with open('dataset.csv', 'w', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # create header
        header = ['title', 'url', 'source_domain', 'description', 'authors', 'date_publish',
                  'average_sentence_polarity', 'maintext']
        writer.writerow(header)

        # create each row
        for key in a.get_keys():
            art = a.get_article(key)
            row = [art.title, art.url, art.source_domain, art.description, art.authors,
                   art.date_published, art.average_sentence_polarity, art.main_text]
            writer.writerow(row)
