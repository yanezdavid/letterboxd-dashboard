import os
import random
import pandas as pd

from errors import Error, LetterboxdException

import dash
from dash import html

import plotly.express as px



# initialize dash app
app = dash.Dash()

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

    # throw error if user has rated less than 100 films
    if len(df) < 100:
        raise LetterboxdException("Must have at least 100 films rated", Error.not_enough_films)

    # add categorical columns
    df["Era"] = df["Year"].apply(lambda x: "20th Century" if x < 2000 else "21st Century") # divides year of release into 20th/21st century


    # histogram
    fig = px.histogram(df, x="Rating", text_auto=True, opacity=.75, width=1200, height=800)
    fig.update_layout(
        xaxis = dict(
            tickmode = "array",
            tickvals = [.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
        )
    )
    fig.update_layout(barmode='group', bargap=0.30, bargroupgap=0.0, title="Distribution of Your Film Ratings", title_x=.5)
    fig.update_xaxes(title_text='Film Rating', ticks="outside", ticklen=10, tickwidth=2, showgrid=True)
    fig.update_yaxes(title_text='Count', ticks="outside", ticklen=10, tickwidth=2, showgrid=True)
    fig.show()

    # bar
    df["Decade"] = df["Year"].apply(lambda x: f"{str(x)[:-1]}0s") # divides year of release into decade

    fig = px.bar(df.groupby(["Decade"]).mean().reset_index(), text_auto=True, x="Decade", y="Rating", width=1200, height=800, opacity=.75,)
    fig.update_layout(yaxis_range=[.5, 5], barmode='group', bargap=0.30, bargroupgap=0.0, title="Your Average Film Rating by Decade of Film Release", title_x=.5)
    fig.update_xaxes(title_text='Decade of Film Release', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)
    fig.update_yaxes(title_text='Average Rating', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)
    fig.show()

    # scatter and regression
    fig = px.scatter(
    df, x='Year', y='Rating', opacity=.75, trendline="ols", trendline_color_override="lightblue"
    )
    fig.show()

    # create app layout
    app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''')
    ])
    
    
if __name__ == "__main__":
    main()
    app.run_server()
    
    