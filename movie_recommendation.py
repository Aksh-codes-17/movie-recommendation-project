import pandas as pd

data = pd.read_csv("movie_datasets.csv")

def recommend_movies(genre):

    filtered_movies = data[data["genres"].str.contains(genre, case=False, na=False)]

    recommended = filtered_movies.sort_values(
        by=["vote_average","popularity"], ascending=False
    )

    if len(recommended) > 0:
        return recommended[[
            "title",
            "release_date",
            "vote_average",
            "genres",
            "overview"
        ]].head(5).to_dict(orient="records")

    else:
        return []
