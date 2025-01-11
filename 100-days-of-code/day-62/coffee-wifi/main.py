from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

COFFEE_RATING = ['☕', '☕☕', '☕☕☕', '☕☕☕☕️', '☕☕☕☕️☕']
WIFI_RATING = ['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
POWER_RATING = ['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField(label='Opening Time e.g. 8:00AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 8:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=COFFEE_RATING, validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=WIFI_RATING, validators=[DataRequired()])
    power_rating = SelectField(label='Power Socket Availability', choices=POWER_RATING, validators=[DataRequired()])

    submit = SubmitField(label='Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [form.cafe.data, 
                form.location.data, 
                form.opening_time.data, 
                form.closing_time.data, 
                form.coffee_rating.data, 
                form.wifi_rating.data, 
                form.power_rating.data]
        with open('./data/cafe-data.csv', mode="a", encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            csv_file.write("\n")
            writer.writerow(data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./data/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run(debug=True)
