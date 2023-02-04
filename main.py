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

    # convert csv to pandas dataframe
    df = pd.read_csv(ratingsPath)

    # initialise plots object
    plots = Plots(df)

    # histogram
    ratingsHistogram = plots.ratingsHistogram()

    # bar
    ratingsByDecadeBar = plots.ratingsByDecadeBar()
    ratingsByYearWatchedBar = plots.ratingsByYearWatchedBar()

    # scatter and regression
    yearRatingsScatterplot = plots.yearRatingsScatterplot()


    # create app layout
    app.layout = html.Div(children=[
    html.H1(children='Letterboxd Dashboard',
            style={'textAlign': 'center'}),

    html.Div(children=f'''Your favorite decade is the {"1940s"}''',
             style={'textAlign': 'left'}),

    html.Div(children='''An Analysis of Your Film Ratings''',
             style={'textAlign': 'center', 'font-family': 'Arial, sans-serif', 'font-size': '18px', 'color': '#7f8c8d', 'margin-bottom': '30px'}),

    html.Div(
        dcc.Graph(figure=ratingsHistogram),
            style={'margin': '0', 'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
    ),
    html.Div(
        dcc.Graph(figure=ratingsByDecadeBar),
            style={'margin': '30px 0', 'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
    ),
    html.Div(
        dcc.Graph(figure=ratingsByYearWatchedBar),
            style={'margin': '30px 0', 'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
    ),
    html.Div(
        dcc.Graph(figure=yearRatingsScatterplot),
            style={'margin': '30px 0', 'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
    )
    ])

    
if __name__ == "__main__":
    main()
    Timer(1, openBrowser("http://127.0.0.1:8050")).start()
    app.run_server()
    