import plotly.express as px
from dataframe import Dataframe


class Plots(Dataframe):
    """Class for creating plotly visualizations."""

    def showRPlot(self, plot):
        """Shows plotly plot."""
        self.plot.show()

    def ratingsHistogram(self):
        """Returns histogram of film ratings."""
        
        ratingsHistogram = px.histogram(self.dataframe, x="Rating", text_auto=True, opacity=.75, width=1200, height=800)

        ratingsHistogram.update_layout(
            xaxis = dict(
                tickmode = "array",
                tickvals = [.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
            )
        )

        ratingsHistogram.update_layout(barmode='group', bargap=0.30, bargroupgap=0.0,
                              title="What Did You Rate Your Films?<br>(Distribution of Ratings)", title_x=.5)

        ratingsHistogram.update_xaxes(title_text='Your Film Ratings', ticks="outside", ticklen=10, tickwidth=2, showgrid=True)
        
        ratingsHistogram.update_yaxes(title_text='Count', ticks="outside", ticklen=10, tickwidth=2, showgrid=True)

        return ratingsHistogram

    def ratingsByDecadeBar(self):
        """Returns bar plot of average film ratings by decade of film release."""
        self.createDecadeColumn()

        avg_ratings = self.dataframe.groupby(["Decade"]).mean().reset_index()
        avg_ratings["Rating"] = avg_ratings["Rating"].round(1)

        ratingsByDecadeBar = px.bar(avg_ratings,
                        text_auto=True, x="Decade", y="Rating", width=1000, height=700, opacity=.75)

        ratingsByDecadeBar.update_layout(yaxis_range=[.5, 5], barmode='group', bargap=0.30, bargroupgap=0.0,
                             title="What is Your Favorite Decade of Cinema?<br>(Average Film Ratings Grouped by Decade of Film Release)",
                             title_x=.5)

        ratingsByDecadeBar.update_xaxes(title_text='Decade of Film Release', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        ratingsByDecadeBar.update_yaxes(title_text='Average Film Ratings', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        return ratingsByDecadeBar

    def ratingsByYearWatchedBar(self):
        """Returns bar plot of average film ratings by decade of film release."""
        self.createYearWatchedColumn()

        avg_ratings = self.dataframe.groupby(["Year Watched"]).mean().reset_index()
        avg_ratings["Rating"] = avg_ratings["Rating"].round(1)

        ratingsByYearWatchedBar = px.bar(self.dataframe.groupby(["Year Watched"]).mean().reset_index(),
                        text_auto=True, x="Year Watched", y="Rating", width=1000, height=700, opacity=.75)

        ratingsByYearWatchedBar.update_layout(yaxis_range=[.5, 5], barmode='group', bargap=0.30, bargroupgap=0.0,
                             title="Did You Rate Films Differently Based on the Year you Watched Them?<br>(Average Film Ratings Grouped by Year Watched)",
                             title_x=.5)

        ratingsByYearWatchedBar.update_xaxes(title_text='Year Film Was Watched', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        ratingsByYearWatchedBar.update_yaxes(title_text='Average Film Ratings', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        return ratingsByYearWatchedBar

    def yearRatingsScatterplot(self):
        """Returns scatterplot of year vs film ratings."""
        yearRatingsScatterplot = px.scatter(self.dataframe, x='Year', y='Rating', opacity=.75, trendline="ols", width=1000, height=700,)
        yearRatingsScatterplot.update_layout(title="Is There a Relationship Between your Film Ratings and the Year of Film Release?<br>(Film Ratings vs Film Release Year)",
                                             title_x=.5)
        yearRatingsScatterplot.update_xaxes(title_text="Year of Film Release", ticks="inside", ticklen=10, tickwidth=2, showgrid=True)
        yearRatingsScatterplot.update_yaxes(title_text="Film Ratings", ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        return yearRatingsScatterplot
