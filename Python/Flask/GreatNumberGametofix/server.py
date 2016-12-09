from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Super duper secret'
import random
from random import randint

@app.route('/')
def index():
    session['random'] = (random.randrange(0, 101))
    print session['random']
    return render_template('index.html')



@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['number'])
    guess = session['guess']

    return render_template('index.html')



@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)
