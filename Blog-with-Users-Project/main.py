from datetime import date
from typing import List

import flask
import flask_login
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(Users).where(Users.id == user_id)).scalar()


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("blog_users.id"))
    author = relationship("Users", back_populates="posts")
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="post")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("blog_users.id"))
    author = relationship("Users", back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    post = relationship("BlogPost", back_populates="comments")

class Users(UserMixin, db.Model):
    __tablename__ = "blog_users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=True)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")


# TODO: Create a User table for all your registered users. 


with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        secure_password = generate_password_hash(registerForm.password.data, method="pbkdf2:sha256", salt_length=8)

        result = db.session.execute(db.select(Users).where(Users.email == registerForm.email.data))
        user = result.scalar()

        if user:
            flash("Email already in use.")
            return redirect(url_for('login'))

        new_user = Users(
            name=registerForm.name.data,
            email=registerForm.email.data,
            password=secure_password
        )

        db.session.add(new_user)
        db.session.commit()

        db.session.refresh(new_user)

        login_user(new_user)

        return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=registerForm)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():

    loginForm = LoginForm()

    if not loginForm.validate_on_submit():
        return render_template("login.html", form=loginForm)

    result = db.session.execute(db.select(Users).where(Users.email == loginForm.email.data))
    user = result.scalar()

    if not user:
        flash("Invalid credentials, please try again.")
        return render_template("login.html", form=loginForm)

    if not check_password_hash(user.password, loginForm.password.data):
        flash("Invalid credentials, please try again.")
        return render_template("login.html", form=loginForm)

    if not login_user(user):
        flash("Invalid credentials, please try again.")
        return render_template("login.html", form=loginForm)

    return redirect(url_for('get_all_posts'))


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()

    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    commentForm = CommentForm()
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()

    if commentForm.validate_on_submit():
        if current_user.is_authenticated:
            comment = Comment(
                body=commentForm.body.data,
                author_id=current_user.id,
                post_id=post_id
            )
            db.session.add(comment)
            db.session.commit()

            redirect(url_for("show_post", post_id=post_id))
        else:
            flash("Please, login to comment.")
            return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, form=commentForm)



# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author_id=post.author_id,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
