from flask.views import View, MethodView

from flask import request, render_template

from robot_app import app

# 1
# class MyViews(View):
#
#     def dispatch_request(self):
#         return "class based ok", 200

# app.add_url_rule('/class/users', view_func=MyViews.as_view('users'))
# _1
# результат http://localhost:4200/class/users
# class based ok

# 2
# class MyViews(View):
#
#     def __init__(self, data, template_name):
#         self.data = data
#         self.template = template_name
#
#     def dispatch_request(self):
#         return f"Data: {self.data}, template: {self.template}", 200
#
# users = ['First', 'Second', 'Third']
#
# app.add_url_rule(
#     '/class/users',
#     view_func=MyViews.as_view('users', users, 'users.html'))
# результат http://localhost:4200/class/users
# Data: ['First', 'Second', 'Third'], template: users.html
# -2

class MyViews(View):
    methods = ['GET', 'POST']

    def __init__(self, data, template_name):

        self.data = data
        self.template = template_name

    def dispatch_request(self):
        if request.method == 'GET':
            return f"Data: {self.data}, template: {self.template}", 200
        else:
            return 'ok it is POST', 201

users = ['First', 'Second', 'Third']
books = ['book1', 'book2','book3']
movies = ['movie1', 'movie2','movie3']

app.add_url_rule(
    '/class/users',
    view_func=MyViews.as_view('class-users', users, 'users.html'))

app.add_url_rule(
    '/class/books',
    view_func=MyViews.as_view('class-books', books, 'books.html'))

app.add_url_rule(
    '/class/movies',
    view_func=MyViews.as_view('class-movies', movies, 'movies.html'))
# результат http://localhost:4200/class/users
# Data: ['First', 'Second', 'Third'], template: users.html



class ListViews(View):
    methods = ['GET', 'POST']

    def __init__(self, model, template_name):

        self.model = model
        self.template = template_name

    def dispatch_request(self):
        if request.method == 'GET':
            # отримувати всіх обэктів
            objects = self.model.get_all()
            return render_template(self.template, objects)


class MyMethodView(MethodView):
    def get(self):
        return 'Method GET ok', 200
    def post(self):
        return 'Method POST ok', 201

app.add_url_rule(
    '/class/methods',
    view_func=MyMethodView.as_view('class-methods')
)
