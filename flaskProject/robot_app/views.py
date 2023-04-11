
import os

from robot_app import app
from flask import request, render_template, make_response, redirect, abort, session, url_for
from .models import User, Book, Purchase
from markupsafe import escape
import werkzeug.exceptions
import json
import jinja2
import random

app.secret_key = os.getenv('SECRET_KEY')


@app.route('/users/<int:user_id>')
def user(user_id):
    id_user = User.query.get(user_id)

    if not id_user:
        return render_template('404.html'), 404
    return render_template('users.html', id_user=id_user)


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/books/<int:book_id>')
def book(book_id):
    id_book = Book.query.get(book_id)
    if not id_book:
        return render_template('404.html'), 404
    return render_template('books.html', id_book=id_book)


@app.route('/purchases')
def purchases():
    purchases = Purchase.query.all()
    return render_template('purchases.html', purchases=purchases)


@app.route('/purchases/<int:purchase_id>')
def purchase(purchase_id):
    id_purchase = Purchase.query.get(purchase_id)
    if not id_purchase:
        return render_template('404.html'), 404
    return render_template('purchases.html', id_purchase=id_purchase)
