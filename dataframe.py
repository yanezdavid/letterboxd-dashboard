import pandas as pd


class Dataframe():
    """
    Class for editing dataframes.

    Attributes
    ----------
    dataframe : Dataframe
        a pandas dataframe object
    """
    def __init__(self, dataframe):
        self.dataframe = dataframe

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
        self.dataframe["Year Watched"] = self.dataframe["Date"].apply(lambda x : "20" + f"{str(x)[-2:]}")
