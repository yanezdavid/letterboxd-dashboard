import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from errors import Error, LetterboxdException


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

    plt.figure(figsize=(14,7))
    plt.hist(x=df["Rating"], color="lightblue", edgecolor="black")
    plt.xticks([.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
    
    plt.xlim([0.5, 5])

    plt.show()
    
if __name__ == "__main__":
    main()
    