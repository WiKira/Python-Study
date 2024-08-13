from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

from werkzeug.exceptions import NotFound

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

api_key = "TopSecretAPIKey"

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        return {column.name: getattr(self, column.name) for column in self.__table__.columns if column.name != "id"}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    with app.app_context():
        cafes = db.session.execute(db.select(Cafe)).scalars().all()
        cafe = choice(cafes)
    return jsonify(cafe={
        # "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "amenities": {
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
    }, status=200, mimetype='application/json')


@app.route("/all", methods=["GET"])
def all():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = cafes.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("location")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location).order_by(Cafe.name))
    all_cafes = cafes.scalars().all()
    if len(all_cafes) > 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    error = {"Not Found": "Sorry, we don't have a cafe at that location."}
    return jsonify({"error": error})


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify({"response": {"success": "Successfully added the new cafe."}})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        with app.app_context():
            cafe = db.get_or_404(Cafe, cafe_id)

            cafe.coffee_price = request.args.get("new_price")
            db.session.commit()
            return jsonify({"response": {"success": "Successfully updated the price."}})
    except Exception:
        return jsonify({"error": {"Not Found": "Sorry a Cafe with that id was not found in the database."}}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if api_key == request.args.get("api_key"):
        try:
            with app.app_context():
                cafe = db.get_or_404(Cafe, cafe_id)
                db.session.delete(cafe)
                db.session.commit()
                return jsonify({"response": {"success": "Successfully deleted the cafe."}})
        except Exception:
            return jsonify({"error": {"Not Found": "Sorry a Cafe with that id was not found in the database."}}), 404
    else:
        return jsonify({"error": {"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}}), 403


if __name__ == '__main__':
    app.run(debug=True)
