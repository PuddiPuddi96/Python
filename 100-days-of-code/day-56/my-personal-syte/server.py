from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Angela')
def get_angela_cv():
    return render_template('Angela.html')

if __name__ == "__main__":
    app.run(debug=True)
