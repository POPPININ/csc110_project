"""Read and write CSV files.


Copyright and Usage Information
===============================
Code by Anna Myllyniemi and Raghav Arora, December 2021
"""
import csv
import datetime
from article_classes import Article, Articles


def read_file(file_path: str) -> Articles:
    """Read csv file and populate Articles object where each row in the csv is an item in
    _articles and corresponds to an Article object.


    Preconditions:
        - file_path != ''
    """
    articles = Articles()
    with open(file_path, mode='r', encoding='UTF8') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            article = Article(
                title=row['title'],
                date_published=datetime.datetime.strptime(
                    row['date_publish'], "%Y-%m-%d %H:%M:%S"
                ),
                authors=row['authors'],
                main_text=row['maintext'],
                source_domain=row['source_domain'],
                url=row['url'],
                average_sentence_polarity=row['average_sentence_polarity'],
                description=row['description']
            )
            articles.add_article(article)

    return articles


def write_file(a: Articles, file_path: str) -> None:
    """ Create a csv file containing all the cleaned data from the web scraping.


    Preconditions:
        - file_path != ''
        - a._articles != {}
    """
    # open the file in the write mode
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
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


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': [],
        'extra-imports': [
            'python_ta.contracts', 'datetime', 'csv', 'article_classes'
        ],
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200', 'E9998']  # E9998 disabled because we read and write files
    })
