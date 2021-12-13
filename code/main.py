"""
This file performs the following tasks:

1. Use the NewsPlease library's web crawler to collect news articles and opinion pieces 
using their URLs from links.txt, 

2. Clean and process the data crawled, and represent each news article and opinion piece as an Article object, 
which can be collectively accessed through an Articles object via a mapping. Save the processed data into
a file called dataset.csv

3. Read the processed file into an Articles object, and perform sentiment analysis on each 
Article's text using NLTK. We assign the sentiment score to the Article's 
'average_sentence_polarity' attribute. Finally, we save the result into a file called
analyzed_articles.py

3. Filter and classify the articles based on the themes discussed (e.g. Vaccine passport, travel bubbles,
Federal COVID-19 policies etc.), sort articles belonging to each theme by date published, and presenting
our findings using Plotly.

------------------------------------------------------------------------
Code by Anna Myllyniemi, Raghav Arora, Aarya Vatsa and Diva Hidalgo Luna
------------------------------------------------------------------------
"""
import pandas as pd
import plotly
import plotly.io as pio
import plotly.express as px


from create_dataset import create_dataset
from csv_read_write import read_file, write_file

# creates the dataset including web scraping, cleaning, sentiment analysis, etc. Will take a
# VERY long time to run. Approximately 5 minutes.
# Only uncomment if you need to recreate the dataset.
"""create_dataset(
    links_path='../data/links.txt',
    dataset_save_path='../data/dataset.csv'
)"""

# Load the Dataset CSV file
articles = read_file('../data/dataset.csv')  # Load cleaned and processed data into Articles object
articles.run_sentiment()  # Perform sentiment analysis on each article
write_file(articles, '../data/analyzed_articles.csv')  # save the analyzed articles

print(articles._articles)

# put code here to run graphing files
df = pd.read_csv('../data/analyzed_articles.csv')

# VACCINE PLOT
vaccine_df = df[df['maintext'].str.contains('vaccine')]

scatterplot = px.scatter(
    data_frame=vaccine_df,
    x='date_publish',
    y='average_sentence_polarity',
    color='average_sentence_polarity',
    color_continuous_scale=px.colors.diverging.Temps,
    hover_name='title',
    hover_data=['url', 'source_domain'],

    range_y=['March 2020', 'December 2021'],
    title="'Vaccine' Keyword Scatterplot"
)

pio.show(scatterplot)

# MASK PLOT
mask_df = df[df['maintext'].str.contains('mask')]

scatterplot = px.scatter(
    data_frame=mask_df,
    x='date_publish',
    y='average_sentence_polarity',
    color='average_sentence_polarity',
    color_continuous_scale=px.colors.diverging.Temps,
    hover_name='title',
    hover_data=['url', 'source_domain'],

    range_y=['March 2020', 'December 2021'],
    title="'Mask' Keyword Scatterplot"
)

pio.show(scatterplot)

# MANDATE PLOT
mandate_df = df[df['maintext'].str.contains('mandate')]

scatterplot = px.scatter(
    data_frame=mandate_df,
    x='date_publish',
    y='average_sentence_polarity',
    color='average_sentence_polarity',
    color_continuous_scale=px.colors.diverging.Temps,
    hover_name='title',
    hover_data=['url', 'source_domain'],

    range_y=['March 2020', 'December 2021'],
    title="'Mandate' Keyword Scatterplot"
)

pio.show(scatterplot)

# RESTRICTION PLOT
restriction_df = df[df['maintext'].str.contains('restriction')]

scatterplot = px.scatter(
    data_frame=restriction_df,
    x='date_publish',
    y='average_sentence_polarity',
    color='average_sentence_polarity',
    color_continuous_scale=px.colors.diverging.Temps,
    hover_name='title',
    hover_data=['url', 'source_domain'],

    range_y=['March 2020', 'December 2021'],
    title="'Restriction' Keyword Scatterplot"
)

pio.show(scatterplot)

# BORDER_CLOSURE PLOT
bc_df = df[df['maintext'].str.contains('border closure' or 'border' or 'closure')]

scatterplot = px.scatter(
    data_frame=bc_df,
    x='date_publish',
    y='average_sentence_polarity',
    color='average_sentence_polarity',
    color_continuous_scale=px.colors.diverging.Temps,
    hover_name='title',
    hover_data=['url', 'source_domain'],

    range_y=['March 2020', 'December 2021'],
    title="'Border' Closure Keyword Scatterplot"
)

pio.show(scatterplot)
