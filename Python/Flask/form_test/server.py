from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True) # run our server

'''from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '\x14\xf8\x85P\xe8\x10\xc7\x8f\xe7\xdc6D\x8c,\xa5\x9c\xd8\xbb\xbdsi\xa0N['
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users', methods=['POST'])
def create_user():
    print 'Got Post Info'
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')
@app.route('/show')
def show_user():
    return render_template('users.html', name=session['name'])
app.run(debug=True)'''
