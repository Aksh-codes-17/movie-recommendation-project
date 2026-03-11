import pandas as pd
data = pd.read_csv("movie_datasets.csv")

print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("--------------------------------")
print("\nAvailable Movies:\n")
print(data[["title","release_date","vote_average","genres","popularity"]].head(10))
genre = input("\nEnter a genre (Action, Comedy, Drama etc): ")
filtered_movies = data[data["genres"].str.contains(genre, case=False, na=False)]
recommended = filtered_movies.sort_values(by=["vote_average","popularity"], ascending=False)

print("\n⭐ Top Recommended Movies:\n")

if len(recommended) > 0:
    print(recommended[[
        "title",
        "release_date",
        "vote_average",
        "vote_count",
        "genres",
        "overview"
    ]].head(5))
else:

    print("❌ No movies found for this genre.")
