#!/usr/bin/env python3
from flask import Flask, flash, render_template, session, redirect, request, url_for
import os
import functools

app = Flask(__name__)
app.secret_key = os.urandom(24)

############################################################################

slova = ('Thanos', 'eee', 'Toy Story', '177013')


def prihlasit(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return function(*args, **kwargs)
        else:
            return redirect(url_for('login', url=request.path))
    return wrapper
############################################################################


@app.route('/',methods=["GET"])
def login():
    return render_template('login.html')


@app.route('/',methods=["POST"])
def login_post():
    login=request.form.get("login")
    passwd=request.form.get("passwd")
    if login=='lolienthusiast69' and passwd=='eeeee':
        session['login']=login
        flash('prihlasen')
    else:
        flash('Špatně!')
    return render_template('login.html')


@app.route('/ond/')
def ond():
    return render_template('ond.html')


############################################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)
