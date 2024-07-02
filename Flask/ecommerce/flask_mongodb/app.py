from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['userDB']
users_collection = db['users']


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username already exists
        if users_collection.find_one({'username': username}):
            return 'Username already exists!'

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert user data into MongoDB
        users_collection.insert_one({'username': username, 'password': hashed_password})

        return redirect(url_for('login'))
    return render_template('register.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists
        user = users_collection.find_one({'username': username})
        if user:
            # Check password
            if check_password_hash(user['password'], password):
                session['username'] = username
                return redirect(url_for('profile'))

        return 'Invalid username or password!'
    return render_template('login.html')


# Profile route
@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    return redirect(url_for('login'))


# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
