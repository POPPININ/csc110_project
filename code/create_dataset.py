"""
Creates a CSV file containing data scraped from news articles. Scrapes websites using NewsPlease,
cleans the maintext, and creates the csv file.


Copyright and Usage Information
===============================
Code by Anna Myllyniemi, December 2021
"""
import datetime
from newsplease import NewsPlease
from csv_read_write import write_file
from article_classes import Article, Articles


def create_dataset(links_path: str, dataset_save_path: str) -> None:
    """Calling this function from main.py calls all the necessary functions to scrape the news
    articles, clean the data, and save it into a csv file.

    Preconditions:
        - links_path != '' and dataset_save_path != ''
    """
    scraped_arts = NewsPlease.from_file(links_path)
    articles = setup_articles(scraped_arts)
    clean_dataset(articles)
    write_file(articles, dataset_save_path)


def setup_articles(scraped_articles: dict) -> Articles:
    """Takes the dictionary from the scraper and creates a populated articles object that will be
    later cleaned.


    Preconditions:
        - scraped_articles != {}
    """
    a = Articles()
    for key in scraped_articles.keys():
        scr_art = scraped_articles[key]
        art = Article(
            title=scr_art.title,
            date_published=scr_art.date_publish,
            authors=scr_art.authors,
            main_text=scr_art.maintext,
            source_domain=scr_art.source_domain,
            url=scr_art.url,
            description=scr_art.description
        )
        a.add_article(art)

    return a


def clean_dataset(arts: Articles) -> None:
    """ Mutates and cleans data in articles.


    Preconditions:
        - arts._articles != {}
    """
    for key in arts.get_keys():
        article = arts.get_article(key)

        if article.main_text is not None:
            article.main_text = clean_maintext(article)
        else:
            article.main_text = ''

        if article.title is not None:
            article.title = fix_unicode(article.title)
        else:
            article.title = ''

        if article.description is not None:
            article.description = fix_unicode(article.description)
        else:
            article.description = ''

        if article.date_published is None:
            article.date_published = datetime.datetime(2000, 1, 1)


def clean_maintext(article: Article) -> str:
    """ Clean maintext of article by removing content unrelated to the body of the article and
    reformating. Returns the cleaned maintext.


    Preconditions:
        - article is not None
        - article.main_text != ''
    """

    # list of common strings to remove from maintext that are not part of the article body.
    remove = ['This advertisement has not loaded yet, but your article continues below.',
              'Share this Story:',
              'Advertisement Story continues below',
              'This advertisement has not loaded yet, '
              'but your article continues below.',
              'We apologize, but this video has failed to load.',
              'Try refreshing your browser.',
              'Share this article in your social network',
              'Latest National Stories',
              'News Near Portage',
              'The news seems to be flying at us faster all the time. From COVID-19 updates to '
              'politics and crime and everything in between, it can be hard to keep up. With that '
              'in mind, the Regina Leader-Post has created an Afternoon Headlines newsletter that '
              'can be delivered daily to your inbox to help make sure you are up to date with the '
              'most vital news of the day. Click here to subscribe.',
              'tap here to see other videos from our team.',
              'Back to video',
              'Try refreshing your browser, or',
              ]

    # split text by 'Article content' and remove first index of the list if it contains
    # content irrelevant to the body of the article, and also remove subscription related text
    # at the end
    if 'Article content' in article.main_text:
        split_text = article.main_text.split('Article content')

        if 'Photo by' in split_text[0] or 'Postmedia' in split_text[0]:
            split_text.pop(0)  # remove start blurb

        if 'Share this article in your social network' in split_text[-1]:
            split_text[-1] = split_text[-1][0: split_text[-1].find
                                            ('Share this article in your social network')]
            # remove blurb at end regarding subscriptions
        clean = ''.join(split_text)
    else:
        clean = article.main_text

    title = article.title
    description = article.description

    clean = clean.replace(title, '')  # remove occurences of title in text

    if description is not None:
        clean = clean.replace(description, '')  # remove description from maintext

    # loop through the list of strings to remove
    for r in remove:
        clean = clean.replace(r, '')

    clean = fix_unicode(clean)
    clean = ' '.join(clean.split())  # replace multiple whitespaces with a single whitespace

    return clean


def fix_unicode(text: str) -> str:
    """ Clean characters.


    Preconditions:
        - text != ''
    """
    clean = text.replace('’', '\'')  # replace apostrophes with single quotation
    clean = clean.replace('\n\n', '\n')  # replace two newlines with one newline
    clean = clean.replace('“', '\"')  # replace double quotes with escaped double quotes
    clean = clean.replace('”', '\"')  # replace double quotes with escaped double quotes
    clean = clean.replace('—', '-')
    clean = clean.replace('–', '-')
    clean = clean.replace('é', 'e')
    clean = clean.replace('‘', '\'')

    return clean


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': [
            'python_ta.contracts', 'datetime', 'newsplease', 'csv_read_write', 'article_classes'
        ],
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200']
    })
