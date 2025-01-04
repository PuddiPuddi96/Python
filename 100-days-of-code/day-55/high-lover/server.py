from flask import Flask
from random import randint

app = Flask(__name__)

number_to_guess = 0

def generate_random_number():
    return randint(0, 9)

@app.route('/')
def home():
    global number_to_guess
    number_to_guess = generate_random_number()
    print(number_to_guess)
    return """
            <h1>Guess a number between 0 and 9</h1>
            <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />
    """

@app.route('/<int:number>')
def guess_number(number:int):
    if number_to_guess > number:
        return """
                <h1 style="text-color: red">Too low, try again!</h1>
                <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />
        """
    elif number_to_guess < number:
        return """
                <h1 style="text-color: purple">Too high, try again!</h1>
                <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />
        """
    else:
        return """
                <h1 style="text-color: green">You found me!</h1>
                <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />
        """


if __name__ == "__main__":
    app.run(debug=True)
