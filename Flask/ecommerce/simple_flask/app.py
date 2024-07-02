from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the home page!'


@app.route('/about')
def about():
    return 'This is the about page.'


@app.route('/user/<username>')
def user_profile(username):
    return 'Hello, {}!'.format(username)


if __name__ == '__main__':
    app.run(debug=True)
