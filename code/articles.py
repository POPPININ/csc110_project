"""
Access and mapping Article objects via a mapping.
"""
from article import Article
from datetime import datetime
from analyze_sentiment import calculate_average_polarity
import csv


class Articles:
    """Key-value mapping of Article Title and Author(s) to the corresponding Article object.
    
    Instance Attributes:
       - articles: a dictionary containing key-value mappings of (title, authors) to Article
       objects.
    """
    _articles = {}

    def __init__(self, file_path: str):
        """Initialise dataclass object using the corresponding dictionary representation 
        of information."""
        with open(file_path, mode ='r') as file: 
            csv_file = csv.DictReader(file)
            for row in csv_file:
                self._articles[(row['title'], row['authors'])] = Article(
                    title=row['title'],
                    date_published=datetime.strptime(row['date_publish'], "%Y-%m-%d %H:%M:%S"),
                    authors=row['authors'],
                    main_text=row['maintext'],
                    average_sentence_polarity=calculate_average_polarity(row['maintext'])
                )