from flask import render_template, request
from app import app

@app.route('/')
def homepage():
    name = request.args.get('name')
    if not name:
        name = '<unknown>'
    # see at http://localhost:5000/?name=Simon
    # move to Loops, control structures, and template programming
    return render_template('homepage.html', name=name)
