import pandas as pd

# Load dataset
data = pd.read_csv("movie_datasets.csv")

print("🎬 MOVIE RECOMMENDATION SYSTEM")
print("--------------------------------")

# Show some movies
print("\nAvailable Movies:\n")
print(data[["title","release_date","vote_average","genres","popularity"]].head(10))

# Ask user for genre
genre = input("\nEnter a genre (Action, Comedy, Drama etc): ")

# Filter movies by genre
filtered_movies = data[data["genres"].str.contains(genre, case=False, na=False)]

# Sort by rating and popularity
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