"""
Dataclass representation of the news articles and opinion pieces
analyzed in our project.
"""
from datetime import datetime
from dataclasses import dataclass


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
    average_sentence_polarity: float