# app/app.py
from flask import Flask, render_template, request
from recommender import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        book_title = request.form["book"]
        recommendations = get_recommendations(book_title)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
