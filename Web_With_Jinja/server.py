import datetime
import requests
from flask import Flask, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html',
                           num=randint(1, 10),
                           current_year=datetime.datetime.now().year,
                           built_by="William C. S. Camargo")


def get_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()["gender"]


def get_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()["age"]


@app.route('/guess/<string:name>')
def guess_page(name: str):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html",
                           name=name.title(),
                           gender=gender,
                           age=age)

@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)