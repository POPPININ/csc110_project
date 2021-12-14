# CSC110 Project

## Group Members

Raghav Arora, Anna Myllyniemi, Diva Hidalgo Luna and Aarya Vatsa

## Installation

We have supplied a simple batch file for Windows users, ```start.bat```, which may be executed to set up a virtual environment, install the required dependencies and get you going. MacOS users may write an equivalent script.

**NOTE**: We have used the NLTK library to perform sentiment analysis, and the particular functions we used require downloading 'punkt' and 'vader_lexicon'. You may use the Python terminal to download the required files


```python
import nltk

nlkt.download('punkt')
nlkt.download('vader_lexicon')
```