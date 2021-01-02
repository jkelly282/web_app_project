from app import app
from flask import render_template, flash, redirect, url_for

from app.forms import LoginForm


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.username.data}, remember_me={form.remember_me.data},'
              f' password = {form.password.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
