from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'RODRIGO'}
    posts = [
        {
            'author': {'username': 'Barack Obama'},
            'body': 'Derby County are an abysmal team and such a nasty bunch of people it makes me think Republicans are not that bad!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'I agree with my main man Barack '
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)