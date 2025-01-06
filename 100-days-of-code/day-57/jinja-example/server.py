from flask import Flask, render_template
from random import randint
from datetime import datetime
from requests import get

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"

app = Flask(__name__)

@app.route('/')
def home():
    random_number = randint(1, 10)
    current_year = datetime.now().year
    return render_template('index.html', num = random_number, year=current_year)

agify_params = {
    "name": "Davide"
}

genderize_params = {
    "name": "Davide"
}


@app.route('/guess/<string:name>')
def guess_age_gender(name:str):
    current_year = datetime.now().year

    agify_response = get(AGIFY_URL, params=agify_params).json()
    age = agify_response["age"]

    genderize_response = get(GENDERIZE_URL, params=genderize_params).json()
    gender = genderize_response["gender"]

    return render_template('guess.html', name=name, age=age, gender=gender, year=current_year)

@app.route('/blog')
def get_blog():
    return render_template('blog.html', posts=__get_posts())


def __get_posts():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    respose = get(blog_url)
    return respose.json()

if __name__ == "__main__":
    app.run(debug=True)
