from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "super duper secret"
session = {
"count": 0
}
@app.route('/', methods=['GET'])
def counter():
    session['count'] += 1

    return render_template('index.html', count=session['count'])

@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')


app.run(debug=True)
