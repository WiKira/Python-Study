import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        result = db.session.execute(db.select(User).where(User.email == request.form.get("email")))
        user = result.scalar()

        if user:
            flash('E-mail already in use. Please Log-in')
            return render_template("register.html")

        secured_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        new_user = User(
            email=request.form.get("email"),
            name=request.form.get("name"),
            password=secured_password
        )

        db.session.add(new_user)
        db.session.commit()

        return render_template("secrets.html", username = new_user.name, logged_in=new_user.is_authenticated)
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        result = db.session.execute(db.select(User).where(User.email == request.form.get('email')))
        user = result.scalar()
        if check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            print(user)
            return redirect(url_for('secrets', username=user.name, logged_in=current_user.is_authenticated))
        flash('Invalid password provided')
        return render_template("login.html")
    return render_template("login.html")


@login_required
@app.route('/secrets')
def secrets():
    if not current_user.is_authenticated:
        return login_manager.unauthorized()

    return render_template("secrets.html", username=current_user.name, logged_in=current_user.is_authenticated)


@login_required
@app.route('/logout')
def logout():
    if not current_user.is_authenticated:
        return login_manager.unauthorized()

    if not current_user.is_authenticated:
        return redirect(url_for('home'))
    logout_user()
    return redirect(url_for('home'))


@login_required
@app.route('/download')
def download():
    if not current_user.is_authenticated:
        return login_manager.unauthorized()

    return send_from_directory(
        './static/files/', 'cheat_sheet.pdf', as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
