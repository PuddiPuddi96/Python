from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Form(FlaskForm):
    email = EmailField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        Length(min=8, max=20),
        DataRequired()])
    submit = SubmitField(label='Log In')
