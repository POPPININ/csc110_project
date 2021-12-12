"""
Dataclass representation of the news articles and opinion pieces
analyzed in our project.

code by anna and raghav
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
       - authors: the name of the author(s)
       - main_text: the actual content of the article/OPed
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
       - articles: a dictionary containing key-value mappings of (title, authors) to Article
       objects.
    """
    _articles: dict[str, Article]

    def __init__(self) -> None:
        """Initialises an empty Articles object"""
        self._articles = {}

    def add_article(self, article: Article):
        """Add article to _articles dictionary"""
        self._articles[article.title] = article

    def get_keys(self) -> set[str]:
        """Return keys of _articles"""
        return set(self._articles.keys())

    def get_article(self, key: str) -> Article:
        """Return the Article instance corresponding to key"""
        return self._articles[key]

    def run_sentiment(self) -> None:
        """ Add docstring"""
        for key in self._articles:
            self._articles[key].average_sentence_polarity = \
                calculate_average_polarity(self._articles[key].main_text)
