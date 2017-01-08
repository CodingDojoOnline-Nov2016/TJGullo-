from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from datetime import datetime
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\-]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'loginstuff')
app.secret_key = "super secret key"

@app.route('/', methods=['GET'])
def index():
 return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    print "*"*50
    now = datetime.now()
    print type(now)
    print now.strftime('%m-%d-%Y')
    print "*"*50


    errors = []
 # run validations and if they are successful we can create the password hash with bcrypt
    if len(request.form['first_name']) < 2:
            errors.append('You must enter a First Name of at least 2 characters!')
    elif not NAME_REGEX.match(request.form['first_name']):
            errors.append('Your first name may not contain any special characters or numbers!')

    if len(request.form['last_name']) < 2:
        errors.append('You must enter a Last Name of at least 2 characters!')
    elif not NAME_REGEX.match(request.form['last_name']):
        errors.append('Your last name may not contain any special characters or numbers!')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Your Email Address entry is invalid')

    if len(request.form['password']) < 8:
        errors.append('Your Password must contain 8 or more characters!')

    if request.form['password'] != request.form['confirm']:
        errors.append('Confirm Password and Password must match!')

    print errors
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')

    else:
        flash("Success!")
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
 # now we insert the new user into the database
        data = {
        'email': request.form['email'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'pw_hash': pw_hash,
        }
        query = "INSERT INTO users (email, first_name, last_name, pw_hash, created_at) VALUES (:email, :first_name, :last_name, :pw_hash, NOW())"

        mysql.query_db(query, data)
 # redirect to success page
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    errors = []
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    data = {
	   'email': email,
       }
    user = mysql.query_db(user_query, data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        flash('Successful Login!')
        return redirect('/')
    else:
        flash('Invalid Email!')
        return redirect('/')

        if len(email) < 1 or len(password) < 1:
        	errors.append('All fields must be filled out correctly!')
        elif not EMAIL_REGEX.match(email):
    		errors.append('Must be a valide email address!')
        elif len(password)< 8:
        	errors.append('Password must be at least 8 characters long!')

    	if errors:
    		for error in errors:
    			flash(error)
    		return redirect('/')
    	else:
    		flash('Success!')



    	return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    query = "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email, pw_hash=:pw_hash, updated_at=NOW() WHERE id=:id"
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id': request.form['id']
    }
    print "check it out! --->", mysql.query_db(query, data)
    return redirect('/')


@app.route('/delete/<id>', methods=['POST'])
def destroy(id):
    query = 'DELETE FROM users WHERE id = :id'
    data = { 'id': request.form['id'] }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
