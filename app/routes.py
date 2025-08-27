from flask import Blueprint, render_template, request
from recommender import get_recommendations

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        book_title = request.form.get('book')

        recommendations = get_recommendations(book_title)
    return render_template('index.html', title="BookTrail")


