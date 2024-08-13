import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()
        return render_template('index.html', books=all_books)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            book_to_update.rating = float(request.form.get('rating'))
            db.session.commit()
            return redirect('/')

    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == id).order_by(Book.title)).scalar()
        return render_template('edit.html', book=book)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(title=request.form.get('title'), author=request.form.get('author'), rating=float(request.form.get('rating')))
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    return render_template('add.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

