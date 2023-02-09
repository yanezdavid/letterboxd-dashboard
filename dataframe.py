import pandas as pd
from errors import LetterboxdException, Error


class Dataframe():
    """
    Class for editing pandas dataframes.

    Attributes
    ----------
    dataframe : Dataframe
        a pandas dataframe object
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe
        if len(self.dataframe) < 100:
            raise LetterboxdException("Must have at least 100 films rated", Error.not_enough_films)
        self.removeNull()
        self.dropLetterboxdURI()

    def getDataframe(self):
        """Returns dataframe."""
        return self.dataframe

    def setDataframe(self, newDataframe):
        """Sets dataframe."""
        self.dataframe = newDataframe

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
