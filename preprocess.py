from bs4 import BeautifulSoup
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class Preprocess():
    """Class for preprocessing text data for NLP."""
    def __init__(self):
        pass

    def remove_html(self, text):
        """Removes html tags from a string."""
        soup = BeautifulSoup(text, "lxml")
        stripped_text = soup.get_text()
        return stripped_text

    def remove_punctuation(self, text):
        """Removes punctuation from a string."""
        no_punct_text = "".join([char for char in text if char not in string.punctuation])
        return no_punct_text

    def initialise_tokenizer(self):
        """Initialises tokenizer."""
        tokenizer = RegexpTokenizer(r"\w+")
        return tokenizer

    def tokenize_text(self, text):
        tokenizer = self.initialise_tokenizer()

    def remove_stopwords(self, text):
        """Removes stopwords from an array of strings."""
        words = [word for word in text if word not in stopwords.words("english")]
        return words

    def initialise_lemmatizer(self):
        lemmatizer = WordNetLemmatizer()
        return lemmatizer

    def lemmatize_text(self, text):
        """Lemmatizes an array of strings"""
        lemmatizer = self.initialise_lemmatizer()
        lemmatized_text = " ".join([lemmatizer.lemmatize(word) for word in text])
        return lemmatized_text
        