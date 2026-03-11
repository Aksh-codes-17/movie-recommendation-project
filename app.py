from flask import Flask, render_template, request
from movie_recommendation import recommend_movies

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    movies = []

    if request.method == "POST":
        genre = request.form["genre"]
        movies = recommend_movies(genre)

    return render_template("index.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
