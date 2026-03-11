from flask import Flask, render_template, request, jsonify
from movie_recommendation import recommend_movie

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    movie = request.json["movie"]
    result = recommend_movie(movie)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
