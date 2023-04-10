
import os
import werkzeug.exceptions
import json
import jinja2
import random
import flask

from robot_app import app, db
from flask import request, render_template, make_response, redirect, abort, session, url_for
from .models import User, JobUnit
from markupsafe import escape

app.secret_key = os.getenv('SECRET_KEY')

name_list = ['Bob', 'Tony', 'Taras', 'Anna', 'Jane']
book_list = ["The Great Gatsby", "1984", "The Lord of the Rings", "The Hobbit", "Kobzar"]


@app.get('/users')
def get_name():
    current = session.get('user')
    if current:
        rand_len = random.randint(1, len(name_list))
        res = random.SystemRandom().sample(name_list, rand_len)
        return render_template('/users.html', res=res, username=current)
    else:
        return redirect(url_for('reg_form'))


@app.get('/books')
def get_book():
    current = session.get('user')
    if current:
        res = random.SystemRandom().sample(book_list, random.randint(1, len(book_list)))
        return render_template('/books.html', res=res, username=current)
    else:
        return redirect(url_for('reg_form'))


@app.get('/books/<string:title>')
def get_books(title):
    current = session.get('user')
    if current:
        up_res = title.title()
        return render_template('/books.html', up_res=up_res, username=current)
    else:
        return redirect(url_for('reg_form'))


@app.get('/users/<int:name_id>')
def get_users(name_id):
    current = session.get('user')
    if current:
        return render_template('/user_id.html', name_id=name_id, username=current)
    else:
        return redirect(url_for('reg_form'))






@app.route('/params')
def html_table_parameters():
    current = session.get('user')
    if current:
        params_dict = request.args.to_dict()
        return render_template('/params.html', item=params_dict.items())
    else:
        return redirect(url_for('reg_form'))


@app.route('/login', methods=['GET', 'POST'])
def reg_form():
    if request.method == 'GET':
        return render_template('/login.html')
    elif request.method == 'POST':
        app.logger.info(request.form.get('username'))
        username = request.form.get('username')
        session['user'] = username
        return redirect(url_for('current_user'))
    else:
        return 'ok else', 400


@app.route('/current-user')
def current_user():
    current = session.get('user')
    if current:
        return current
    else:
        return redirect(url_for('reg_form'))
