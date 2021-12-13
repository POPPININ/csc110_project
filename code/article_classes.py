"""
Dataclass representation of the news articles and opinion pieces
analyzed in our project.


Copyright and Usage Information
===============================
Code by Anna Myllyniemi and Raghav Arora, December 2021
"""
from datetime import datetime
from dataclasses import dataclass
from analyze_sentiment import calculate_average_polarity
from typing import Optional


@dataclass
class Article:
    """Representation of a news article/column, opinion piece (OPed), blog etc.

    Instance Attributes:
       - title: The title of the article/OPed
       - date_published: The date the given article/OPed was published
       - authors: the name of the author(s) (as a list)
       - main_text: the actual content of the article/OPed
       - source_domain: the source of news article/OPed
       - url: the URL of the article
       - description: brief description of the news article/OPed
       - average_sentence_polarity: the average polarity of the article based on the mean of the
       polarity of each sentence in the article.
    """
    title: str
    date_published: datetime
    authors: list[str]
    main_text: str
    source_domain: str
    url: str
    description: str
    average_sentence_polarity: Optional[float] = 0.0


class Articles:
    """Key-value mapping of Article Title and Author(s) to the corresponding Article object.

    Instance Attributes:
       - _articles: a dictionary containing key-value mappings of title to Article
       objects.
    """
    _articles: dict[str, Article]

    def __init__(self) -> None:
        """Initialises an empty Articles object."""
        self._articles = {}

    def add_article(self, article: Article) -> None:
        """Add article to _articles dictionary."""
        self._articles[article.title] = article

    def get_keys(self) -> set[str]:
        """Return keys of _articles."""
        return set(self._articles.keys())

    def get_article(self, key: str) -> Article:
        """Return the Article instance corresponding to key."""
        return self._articles[key]

    def run_sentiment(self) -> None:
        """Compute and assign the polarity of the average sentence in each Article."""
        for key in self._articles:
            self._articles[key].average_sentence_polarity = \
                calculate_average_polarity(self._articles[key].main_text)


if __name__ == '__main__':
    import python_ta
    import doctest
    import python_ta.contracts

    doctest.testmod()
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'allowed-io': ['run_example'],
        'extra-imports': [
            'python_ta.contracts', 'datetime', 'dataclass', 'analyze_sentiment', 'typing'
        ],
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['R1705', 'C0200']
    })
