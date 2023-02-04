import plotly.express as px
from dataframe import Dataframe


class Plots(Dataframe):
    """Class for creating plotly visualizations."""
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

    def showRatingsHistogram(self):
        """Shows histogram of film ratings."""
        self.ratingsHistogram.show()

    def ratingsByDecadeBar(self):
        """Returns bar plot of average film ratings by decade of film release."""
        self.createDecadeColumn()

        ratingsByDecadeBar = px.bar(self.dataframe.groupby(["Decade"]).mean().reset_index(),
                        text_auto=True, x="Decade", y="Rating", width=1200, height=800, opacity=.75)

        ratingsByDecadeBar.update_layout(yaxis_range=[.5, 5], barmode='group', bargap=0.30, bargroupgap=0.0,
                             title="What is Your Favorite Decade of Cinema?<br>(Your Average Film Ratings grouped by Decade of Film Release)",
                             title_x=.5)

        ratingsByDecadeBar.update_xaxes(title_text='Decade of Film Release', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        ratingsByDecadeBar.update_yaxes(title_text='Your Average Film Ratings', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        return ratingsByDecadeBar

    def showRatingsByDecadeBar(self):
        """Shows bar plot of average film ratings by decade of film release."""
        self.ratingsByDecadeBar().show()

    def ratingsByYearWatchedBar(self):
        """Returns bar plot of average film ratings by decade of film release."""
        self.createYearWatchedColumn()

        ratingsByYearWatchedBar = px.bar(self.dataframe.groupby(["Year Watched"]).mean().reset_index(),
                        text_auto=True, x="Year Watched", y="Rating", width=1200, height=800, opacity=.75)

        ratingsByYearWatchedBar.update_layout(yaxis_range=[.5, 5], barmode='group', bargap=0.30, bargroupgap=0.0,
                             title="Does the Year You Watched Films in Affect Your Rating of Them?<br>(Your Average Film Ratings grouped by the Year You Watched Them)",
                             title_x=.5)

        ratingsByYearWatchedBar.update_xaxes(title_text='Year You Watched Film', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        ratingsByYearWatchedBar.update_yaxes(title_text='Your Average Film Ratings', ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        return ratingsByYearWatchedBar

    def showRatingsByYearWatchedBar(self):
        """Shows bar plot of average film ratings by decade of film release."""
        self.ratingsByYearWatchedBar().show()


    def yearRatingsScatterplot(self):
        """Returns scatterplot of year vs film ratings."""
        yearRatingsScatterplot = px.scatter(self.dataframe, x='Year', y='Rating', opacity=.75, trendline="ols",
                                trendline_color_override="lightblue", width=1200, height=800,)

        yearRatingsScatterplot.update_xaxes(title_text="Year of Film Release", ticks="inside", ticklen=10, tickwidth=2, showgrid=True)
        yearRatingsScatterplot.update_yaxes(title_text="Your Film Ratings", ticks="inside", ticklen=10, tickwidth=2, showgrid=True)

        return yearRatingsScatterplot

    def showYearRatingsScatterplot(self):
        """Shows scatterplot of year vs film ratings"""
        self.yearRatingsScatterplot().show()
