import pandas as pd
from errors import LetterboxdException, Error
import os


class Dataframe():
    """
    Class for editing pandas dataframes.

    Attributes
    ----------
    dataframe : Dataframe
        a pandas dataframe object
    """
    def __init__(self, dataframe):
        # basename = os.path.splitext(os.path.basename(pathToCSV))
        # if basename not in ["ratings" , "reviews"]:
        #     raise LetterboxdException("Wrong filename entered, dataframe class accepts \"reviews" "or \"ratings", Error.wrong_filename)
        self.dataframe = dataframe

    def checkLen(self):
        """Raises error if too few films are in the dataframe"""
        if len(self.dataframe) < 100:
            raise LetterboxdException("Must have at least 100 films rated", Error.not_enough_films)

    def createDecadeColumn(self):
        """Creates new Decade column on dataframe."""
        self.dataframe["Decade"] = self.dataframe["Year"].apply(lambda x: f"{str(x)[:-1]}0s")

    def createYearWatchedColumn(self):
        """Creates mew year watched column on dataframe."""
        self.dataframe["Year Watched"] = self.dataframe["Date"].apply(lambda x : str(x[0:4]))

    def removeNull(self):
        """Drops any row with null values in it."""
        if self.dataframe.isnull().any().any():
            self.dataframe.dropNull(self.dataframe)

    def dropLetterboxdURI(self):
        """Drops Letterboxd URI column."""
        self.dataframe.drop(columns=["Letterboxd URI"])
