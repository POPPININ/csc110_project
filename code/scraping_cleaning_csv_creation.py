"""
Creates a CSV file containing data scraped from news articles. Scrapes websites using NewsPlease,
cleans the maintext, and creates the csv file.

Copyright and Usage Information
===============================
Code by Anna Myllyniemi December 2021

"""
from newsplease import NewsPlease
import csv


def make_csv() -> None:
    """ Create a csv file containing all the cleaned data from the web scraping.
    """

    # open the file in the write mode
    with open('dataset.csv', 'w', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # create header
        header = ['title', 'url', 'source_domain', 'description', 'authors', 'date_publish',
                  'maintext']
        writer.writerow(header)

        # create each row
        keys = articles.keys()
        for key in keys:
            row = [articles[key].title, articles[key].url, articles[key].source_domain,
                   articles[key].description, articles[key].authors, articles[key].date_publish,
                   articles[key].maintext]
            writer.writerow(row)


def clean_text(articles: dict) -> None:
    """ Clean maintext of article by removing content unrelated to the body of the article and
    reformating. Mutates articles.
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
              'The news seems to be flying at us faster all the time. From COVID-19 updates to politics and crime and '
              'everything in between, it can be hard to keep up. With that in mind, the Regina Leader-Post has created '
              'an Afternoon Headlines newsletter that can be delivered daily to your inbox to help make sure you are up'
              ' to date with the most vital news of the day. Click here to subscribe.',
              'tap here to see other videos from our team.',
              'Back to video',
              'Try refreshing your browser, or',
              ]

    for key in articles:
        # split text by 'Article content' and remove first index of the list that contains
        # content irrelevant to the body of the article
        if 'Article content' in articles[key].maintext:
            split_text = articles[key].maintext.split('Article content')
            #split_text.pop(0)
            clean = ''.join(split_text)
        else:
            clean = articles[key].maintext

        title = articles[key].title
        description = articles[key].description

        clean = clean.replace(title, '')  # remove occurences of title in text

        if description is not None:
            clean = clean.replace(description, '')  # remove description from maintext

        # loop through the list of strings to remove
        for r in remove:
            clean = clean.replace(r, '')

        # if '\n\n' in clean:
        #     clean = clean[0: clean.rfind('\n\n') + 1]  # remove blurb at end regarding subscriptions

        clean = fix_unicode(clean)

        clean = ' '.join(clean.split())  # replace multiple whitespaces with a single whitespace

        articles[key].maintext = clean  # mutate articles dictionary

def fix_unicode(text: str) -> str:
    """ Clean characters """
    clean = text.replace('’', '\'')  # replace apostrophes with single quotation
    clean = clean.replace('\n\n', '\n')  # replace two newlines with one newline
    clean = clean.replace('“', '\"')  # replace double quotes with escaped double quotes
    clean = clean.replace('”', '\"')  # replace double quotes with escaped double quotes
    clean = clean.replace('—', '-')
    clean = clean.replace('–', '-')
    clean = clean.replace('é', 'e')

    return clean


if __name__ == '__main__':
    # print statements should be removed later. Articles is a global variable atm because it makes
    # it easier to check the data cleaning
    print('scraping articles')
    articles = NewsPlease.from_file('links.txt')
    #articles = NewsPlease.from_url('https://leaderpost.com/opinion/columnists/opinion-more-testing-is-vital-to-contain-pandemic-spread/')
    print('cleaning')
    #clean_text({articles.url: articles})
    clean_text(articles)
    print('making csv')
    make_csv()
