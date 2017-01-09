from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt



email_re = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
def containnumber(string):
    return bool(re.search(r'\d', string))
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'supersecretkey'
mysql = MySQLConnector(app, 'the_wall')

@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users)

@app.route('/comment', methods=['POST'])
def comment():
    query = "INSERT INTO comments (comment, message_id, user_id) VALUES (:comment, :message_id, :user_id)"
    data = {
    'comment': request.form['comment'],
    'message_id': request.form['comment_message'],
    'user_id': session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/error')
def error():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', login_error = 'enter a valid email', all_users = users)

@app.route('/registration', methods=['POST'])
def register():
    firstname = request.form['first']
    lastname = request.form['last']
    email = request.form['email']
    password = request.form['pass']
    passwordcon = request.form['passcon']
    pw_hash = bcrypt.generate_password_hash(password)
    error = False

    if len(firstname)<2:
        error = True
        flash('First name must be more than 2 letters', 'first_name')
    if containnumber(firstname)==True:
        error = True
        flash('Name may not contain a number', 'first_name')
    if len(lastname)<2:
        error = True
        flash('Last name must be more than 2 letters', 'last_name')
    if containnumber(lastname)==True:
        error = True
        flash('Name may not contain a number', 'last_name')
    if len(email)<5:
        error = True
        flash('Email must be longer than 5 letters or numbers')
    if len(password)<8:
        error = True
        flash('Password must be longer than 8 digits', 'password')
    if password != passwordcon:
        error = True
        flash('Passwords must match', 'match_password')
    if not error:
        query = "INSERT INTO users (first_name, last_name, password, email, created_at) VALUES (:first, :last, :pw_hash, :email, NOW())"
        data = {
        'first': request.form['first'],
        'last': request.form['last'],
        'pw_hash': pw_hash,
        'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/')
    return redirect('/')

@app.route('/wall', methods=['GET', 'POST'])
def wall():
        query_message1 = "SELECT message, id FROM messages"
        query_message = mysql.query_db(query_message1)
        comment_query = """SELECT comment, message_id, comments.user_id FROM comments
    join messages
    where comments.message_id = messages.id"""
        comments = mysql.query_db(comment_query)
        email = session['email']
        user_id = session['user_id']
        return render_template('wall.html', email = email, user_id = session['user_id'], messages = query_message, comments = comments)

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password_login']
    email1 = request.form['email_login']
    password_login = request.form['password_login']
    user_query = """SELECT * FROM users where email = :user"""
    query_data = { 'user' : email1 }
    user = mysql.query_db(user_query, query_data) #user returned in a list
    query ="SELECT id, password FROM users WHERE email = :email"
    data = { 'email': email1 }
    users = mysql.query_db(query, data)
    if password == password:
        session['email'] = email1
        session['user_id'] = users[0]['id']
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/submit', methods=['POST'])
def submit():
    query = 'INSERT INTO messages (message, users_id) VALUES (:message, :users_id)'
    data = {
    'message': request.form['message'],
    'users_id': session['user_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)
