import os
import pandas as pd

from errors import Error, LetterboxdException

import dash
from dash import dcc
from dash import html




def main():

    # check for correct file placement and naming
    dataDirPath = os.path.realpath("data")
    files = os.listdir(dataDirPath)
    if "ratings.csv" not in files:
        raise LetterboxdException("ratings.csv required in data dir for dashboard", Error.wrong_filename)
    if len(files) == 0:
        raise LetterboxdException("data dir is empty, ratings.csv required in data dir for dashboard", Error.empty_data)

    ratingsPath = os.path.realpath("data/ratings.csv")

    # drop irrelevant features from dataframe
    df = pd.read_csv(ratingsPath)
    if df.isnull().any().any():
        df.dropNull(df)
    df.drop(columns=["Letterboxd URI"])

    app = dash.Dash()
    app.layout = html.Div([])
    app.run_server(debug=True)
    
if __name__ == "__main__":
    main()
    