from datetime import datetime
import json
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import requests

from custom_forms import EditForm, AddForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_rating.db"

db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int]
    description: Mapped[str]
    rating: Mapped[float]
    ranking: Mapped[int]
    review: Mapped[str]
    img_url: Mapped[str]


with app.app_context():
    db.create_all()


with app.app_context():
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )

    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

    # db.session.add(new_movie)
    # db.session.add(second_movie)
    # db.session.commit()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i

    db.session.commit()

    return render_template("index.html", movies=movies)

@app.route("/edit/<int:film_id>", methods=['GET', 'POST'])
def edit(film_id):
    _form = EditForm()

    if request.method == 'POST':
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == film_id)).scalar()
        movie_to_update.rating = _form.rating.data
        movie_to_update.review = _form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=_form)

@app.route("/select", methods=['GET', 'POST'])
def select():
    films = json.loads(request.args.get('films'))["results"]
    return render_template("select.html", movies=films)

@app.route('/get_movie_details/<id>')
def get_movie_details(id):
    url = "https://api.themoviedb.org/3/authentication"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer API_KEY"
    }

    response = requests.get(url, headers=headers)

    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {"accept": "application/json",
               "Authorization": "Bearer API_KEY"
               }

    response = requests.get(url, headers=headers)
    film = response.json()
    movie_to_add = Movie(
        title=film["title"],
        year=datetime.strptime(film["release_date"], '%Y-%m-%d').year,
        description=film["overview"],
        rating=7.5,
        ranking=7,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500{film["poster_path"]}"
    )

    db.session.add(movie_to_add)
    db.session.commit()

    db.session.refresh(movie_to_add)

    return redirect(url_for('edit', film_id=movie_to_add.id))



def get_films_data(film_name):
    url = "https://api.themoviedb.org/3/authentication"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer API_KEY"
    }

    response = requests.get(url, headers=headers)

    url = f"https://api.themoviedb.org/3/search/movie?query={film_name}&include_adult=false&language=en-US&page=1"

    headers = {"accept": "application/json",
               "Authorization": "Bearer API_KEY"
            }

    response = requests.get(url, headers=headers)
    films = response.text

    return films


@app.route("/add", methods=['GET', 'POST'])
def add():
    add_form = AddForm()

    if request.method == 'POST':
        film_name = add_form.title.data
        films_data = get_films_data(film_name)
        return redirect(url_for('select', films=films_data))
    return render_template("add.html", form=add_form)

@app.route("/delete")
def delete():
    id_to_delete = request.args.get('film_id')
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id_to_delete)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
