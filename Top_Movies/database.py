from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Database():

    def __init__(self, app):
        # CREATE DB
        class Base(DeclarativeBase):
            pass

        self.app = app

        self.db = SQLAlchemy(model_class=Base)

        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies_rating.db"

        self.db.init_app(app)

        class Movie(self.db.Model):
            id: Mapped[int] = mapped_column(primary_key=True)
            title: Mapped[str] = mapped_column(unique=True)
            year: Mapped[int]
            description: Mapped[str]
            rating: Mapped[float]
            ranking: Mapped[int]
            review: Mapped[str]
            img_url: Mapped[str]

        with self.app.app_context():
            self.db.create_all()

    def mock(self):
        with self.app.app_context():
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

            self.db.session.add(new_movie)
            self.db.session.add(second_movie)
            self.db.session.commit()
