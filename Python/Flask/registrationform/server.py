from flask import Flask, flash, render_template, request, redirect, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'super duper secret'


@app.route('/', methods=['GET'])
def index():
    return render_template ("index.html")

@app.route('/process', methods=['POST'])
def process():
    is_valid = True

    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['email'] = request.form['email']
    session['pw'] = request.form['pw']


    if len(request.form['firstname'])<1 or len(request.form['lastname'])<1:
        flash('First and last name cannot be empty!')
        is_valid = False
    if any(char.isdigit() for char in request.form['firstname']) == True:
        flash('First and last name cannot have any numbers')
        is_valid = False
    if any(char.isdigit() for char in request.form['lastname']) == True:
        flash('First and last name cannot have any numbers')
        is_valid = False
    if len(request.form['email'])<1:
        flash('Email cannot be empty!')
        is_valid = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        is_valid = False
    if len(request.form['pw'])<1 or len(request.form['confirmpw'])<1:
        flash('Password cannot be empty!')
        is_valid = False
    if len(request.form['pw'])<9 or  len(request.form['confirmpw'])<9:
        flash('Password cannot be smaller than 8 characters!')
        is_valid = False
    if request.form['pw'] != request.form['confirmpw']:
        flash('Passwords are not matching!')
        is_valid = False
    if is_valid:
        return redirect('/process')
    else:
        flash('Please fill your info properly!')
        return redirect('/')



@app.route('/process')
def show_result():
    return render_template('process.html')

app.run(debug=True)
