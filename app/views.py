from flask import render_template
from app import app

@app.route('/')
@app.route('/signin')
def signin():
    # define some template variables
    title = 'Fab Lab'
    user = {'nickname': 'Jane'}  # test user
    # just to illustrate looping
    stuff = [ {'key1': 'value1', 'key2': 'value2'},
              {'key1': 'bar', 'key2': 'foo'} ]

    return render_template('signin.html', title=title, user=user, stuff=stuff)
