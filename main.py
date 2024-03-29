"""
This file performs the following tasks:

1. Use the NewsPlease library's web crawler to collect news articles and opinion pieces 
using their URLs from links.txt, 

2. Clean and process the data crawled, and represent each news article and opinion piece as an Article object, 
which can be collectively accessed through an Articles object with an underlying a mapping.
Save the processed data into a file called dataset.csv

3. Read dataset.csv into an Articles object, and perform sentiment analysis on each 
Article's text using NLTK. For each article, we assign the sentiment score to its
'average_sentence_polarity' attribute. Finally, we save the result into a file called
analyzed_articles.csv

3. Filter and classify the articles using pandas based on the themes discussed (e.x. Vaccine mandates,
lockdowns and quarantines, border closures, etc.). Present our findings using Plotly in an interactive
way, displaying data with different focuses depending on user input.


Copyright and Usage Information
===============================
Code by Anna Myllyniemi, Raghav Arora, Aarya Vatsa and Diva Hidalgo Luna, December 2021
"""
from create_dataset import create_dataset
from csv_read_write import read_file, write_file
from graphing import draw_graph


# print('Hello! To view our interactive graph, input one of the numbers below:'
#       '\nALL article polarities: \'1\' '
#       '\nFiltered by keyword: \'2\''
#       '\nEXIT viewing: \'0\'')
# num = int(input('Type number: '))

# while num != 0:
#     if num == 1:
#         draw_graph('../data/analyzed_articles.csv', '')
#     elif num == 2:
#         print('You chose to filter by keyword.'
#               '\nExample keywords include topic (ex. vaccine, travel, lockdown)'
#               '\nor locations (ex. Toronto, Vancouver, Alberta)'
#               '\nor publications (ex. National Post, Montreal Gazette, Toronto Sun)')
#         keyword = input('Type keyword: ')
#         draw_graph('../data/analyzed_articles.csv', keyword)
#     else:
#         print('Invalid input!')

#     num = int(input('Type number: '))

# print('Thank you for viewing!')

if __name__ == '__main__':
    # creates the dataset including web scraping, cleaning, sentiment analysis, etc. Will take a
    # VERY long time to run. Approximately 5 minutes.
    # Only uncomment if you need to recreate the dataset.
    create_dataset(links_path='./data/links.txt', dataset_save_path='./data/dataset.csv')

    # Load the Dataset CSV file
    articles = read_file('./data/dataset.csv')  # Load cleaned and processed data into Articles object
    articles.run_sentiment()  # Perform sentiment analysis on each article
    write_file(articles, './data/analyzed_articles.csv')  # save the analyzed articles

    # We created a while loop below to get user prompt and create specialized graphs.
    # But, these six graphs below are comprehensive of our work.

    draw_graph('./data/analyzed_articles.csv', '')
    draw_graph('./data/analyzed_articles.csv', 'vaccine')
    draw_graph('./data/analyzed_articles.csv', 'lockdown')
    draw_graph('./data/analyzed_articles.csv', 'Toronto')
    draw_graph('./data/analyzed_articles.csv', 'National Post')
    draw_graph('./data/analyzed_articles.csv', 'border')
