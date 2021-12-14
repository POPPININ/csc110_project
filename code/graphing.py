"""
Drawing a graph from a given csv filepath with optional keyword for filtering through csv.
This file uses pandas for csv reading and manipulation, and plotly.express and plotly.io
for creating and displaying the graph, respectively.

Optional: statsmodel.api for showing regression lines on the graph. You can uncomment the trendline
in the scatterplot = px.scatter{} block to see.

Copyright and Usage Information
--------------
Code by Aarya Vatsa and Diva Hidalgo Luna, December 2021
--------------

------------------------------------
Pandas 1.3.5 (v1.3.5). Feb. 2020
------------------------------------
Author: The pandas development team
Title: pandas-dev/pandas: Pandas
Publisher: Zenodo
URL: <https://doi.org/10.5281/zenodo.3509134>

------------------------------------
Plotly. 2015
------------------------------------
Author: Plotly Technologies Inc
Title: Collaborative Data Science
Publisher: Plotly Technologies Inc.
URL: <https://plot.ly>

"""
import pandas as pd
import plotly.express as px
import plotly.io as pio


def draw_graph(filepath: str, keyword: str) -> None:
    """Draw graph from a csv with the given filepath, and filtered with keyword. The keyword
    might be an empty string, in which case the graph shows all articles found in the csv.


    Preconditions:
        - filepath != ''
    """

    df = pd.read_csv(filepath)
    df['date_publish'] = pd.to_datetime(df['date_publish'])  # to sort x-axis by date
    title = 'Article Polarity over Time'

    if keyword != '':
        title = f'{title}: Filtered for \'{keyword}\''

        df = df[df['maintext'].str.contains(keyword)]  # filtered df
        url_key = keyword.lower()
        pub_df = df[df['url'].str.contains(url_key.replace(' ', ''))]  # for checking publications
        df.append(pub_df)

    scatterplot = px.scatter(
        data_frame=df,
        x='date_publish',
        range_x=['2020-1-1', '2021-12-30'],
        range_y=[-0.2, 0.4],
        y='average_sentence_polarity',
        hover_name='title',
        hover_data=['url', 'source_domain', 'authors'],
        # trendline='ols',  # uncomment for regression line (uses statsmodels)
        labels={
            'date_publish': 'Date Published',
            'average_sentence_polarity': 'Average Sentence Polarity',
            'source_domain': 'Source Domain',
            'authors': 'Authors'
        },
        title=title,
        template='ggplot2',
        color='average_sentence_polarity',
        color_continuous_scale=px.colors.diverging.Temps
    )
    pio.show(scatterplot)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': [
            'python_ta.contracts', 'plotly.io', 'plotly.express', 'pandas'
        ],
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200']
    })
