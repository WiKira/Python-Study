from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    rating = StringField(name="rating", label="Your Rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(name="review", label="Your Review", validators=[DataRequired()])
    done = SubmitField(name="done", label="Done!")


class AddForm(FlaskForm):
    title = StringField(name="title", label="Movie Title", validators=[DataRequired()])
    add_movie = SubmitField(name="add_movie", label="Add Movie")