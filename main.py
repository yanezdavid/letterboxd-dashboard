import os
import random
import pandas as pd

from errors import Error, LetterboxdException
from openBrowser import openBrowser
from plots import Plots

import dash
from dash import dcc
from dash import html

import plotly.express as px

import webbrowser
import socket

from threading import Timer


# initialize dash app
app = dash.Dash()

# main
def main():

    # check for correct file placement and naming
    dataDirPath = os.path.realpath("data")
    files = os.listdir(dataDirPath)
    if "ratings.csv" not in files:
        raise LetterboxdException("ratings.csv required in data dir for dashboard", Error.wrong_filename)
    if len(files) == 0:
        raise LetterboxdException("data dir is empty, ratings.csv required in data dir for dashboard", Error.empty_data_dir)

    # get csv path
    ratingsPath = os.path.realpath("data/ratings.csv")

    # drop irrelevant features from dataframe
    df = pd.read_csv(ratingsPath)
    if df.isnull().any().any():
        df.dropNull(df)
    df.drop(columns=["Letterboxd URI"])

    # throw error if user has less than 100 rated films
    if len(df) < 100:
        raise LetterboxdException("Must have at least 100 films rated", Error.not_enough_films)

    # initialise plots object
    plots = Plots(df)

    # histogram
    ratingsHistogram = plots.ratingsHistogram()

    # bar
    ratingsByDecadeBar = plots.ratingsByDecadeBar()

    # scatter and regression
    yearRatingsScatterplot = plots.yearRatingsScatterplot()

    # create app layout
    app.layout = html.Div(children=[
    html.H1(children='Letterboxd Dashboard',
            style={'textAlign': 'center'}),

    html.Div(children=f'''Your favorite decade is the {"1940s"}''',
             style={'textAlign': 'left'}),

    html.Div(children='''An Analysis of Your Film Ratings''',
             style={'textAlign': 'center'}),

    dcc.Graph(figure=ratingsHistogram),
    dcc.Graph(figure=ratingsByDecadeBar),
    dcc.Graph(figure=yearRatingsScatterplot),
    ])
    
if __name__ == "__main__":
    main()
    Timer(1, openBrowser("http://127.0.0.1:8050")).start()
    app.run_server()
    