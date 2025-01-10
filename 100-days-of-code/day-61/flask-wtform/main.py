from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from form import Form

VALID_EMAIL = "admin@email.com"
VALID_PASSWORD = "12345678"



app = Flask(__name__)
app.secret_key = "qwflkjnqk423mn2n"

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = Form()
    if login_form.validate_on_submit():
        if login_form.email.data == VALID_EMAIL and login_form.password.data == VALID_PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
