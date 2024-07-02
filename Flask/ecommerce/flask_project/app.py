# main.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World! This is a Flask application.'


if __name__ == '__main__':
    app.run(debug=True)
