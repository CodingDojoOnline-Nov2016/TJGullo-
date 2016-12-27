from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+\.[\w]*$')
app.secret_key = "super secret key"

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    }
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>')
def show(id):
    data = {'id': id}
    query = 'SELECT * FROM friends WHERE id = :id'
    friend = mysql.query_db(query, data)
    return render_template('edit.html', friend=friend[0])

@app.route('/update', methods=['POST'])
def update():
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id"
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': request.form['id']
    }
    print "check it out! --->", mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def destroy(id):
    query = 'DELETE FROM friends WHERE id = :id'
    data = { 'id': request.form['id'] }
    return redirect('/')

app.run(debug=True)
