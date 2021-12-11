"""
Dataclass representation of the news articles and opinion pieces
analyzed in our project.
"""
from dataclasses import dataclass
from datetime import datetime
from analyze_sentiment import calculate_polarity


@dataclass
class Information:
    """News articles and opinion pieces are both considered as 'information' with 
    cerrtain attributes.
    
    Every piece of information has
    1. A title
    2. The date it was published
    3. Name(s) of the author
    """
    title: str
    date_published: datetime
    authors: list
    main_text: str
    average_sentence_polarity: float

    def __init__(self, information: dict):
        """Initialise dataclass object using the corresponding dictionary representation 
        of information."""
        self.title = information['title']
        self.date_published = information['date_publish']  # TODO: Convert string date to datetime
        self.main_text = information['maintext']
        self.average_sentence_polarity = calculate_polarity(self.main_text)