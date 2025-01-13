from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from movie_utils import MovieUtils

MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

#---------- [START] Database configuration ----------#
class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"


db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Create table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# first_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(first_movie)
#     db.session.commit()
#     db.session.add(second_movie)
#     db.session.commit()

#---------- [END] Database configuration ----------#

#---------- [START] FORM TO EDIT ----------#
class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your review', validators=[DataRequired()])

    submit = SubmitField(label='Done')
#---------- [END] FORM TO EDIT ----------#

#---------- [START] FORM TO ADD ----------#
class AddMovieForm(FlaskForm):
    title = StringField(label='Movie title', validators=[DataRequired()])

    submit = SubmitField(label='Add movie')
#---------- [END] FORM TO ADD ----------#

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
        all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        movie_utils = MovieUtils()
        movies = movie_utils.get_movies(title)
        return render_template('select.html', options=movies)
    return render_template('add.html', form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(request.form['rating'])
        movie.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    with app.app_context():
        movie = db.get_or_404(Movie, movie_id)
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    movie_utils = MovieUtils()
    if movie_api_id:
        movie = movie_utils.get_movie_info_by_id(movie_api_id)
        new_movie = Movie(
            title=movie["title"],
            year=movie["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{movie['poster_path']}",
            description=movie["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit"))

if __name__ == '__main__':
    app.run(debug=True)
