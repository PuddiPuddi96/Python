from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func()}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return f"<em>{func()}</em>"
    return wrapper

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/')
def hello_word():
    return """
            <h1 style="text-align: center">Hello, word!</h1>
            <p>This is a paragraph</p>
            <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnltdTV4bHJxOGM5MHJ5bGp4OWJmaXE1ZTl3bm95dWkzb2xpdTdzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Puc4FZWExJc0E/giphy.gif" width="200">
            """

#Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

#Creating variable paths and converting the path to a specified data type
@app.route("/username/<string:name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, You are {number} years old!"

if __name__ == "__main__":
    #Run in debug mode to auto-reload
    app.run(debug=True)
