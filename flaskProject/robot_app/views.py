# файл відповідє за роутинг та функції

from robot_app import app
from flask import request, render_template, make_response, redirect, abort
from markupsafe import escape
# import os
# from markupsafe import escape   екранує запити від небажаного  коду при вводі данних урок 33 у кінці -10хв

import werkzeug.exceptions
import json
import jinja2
import random

# app_path = os.path.abspath(os.path.dirname(__file__))
# template_path = os.path.join(app_path, 'app', 'templates')
# app.template_folder = template_path

@app.route('/hello')
def hello():
    app.logger.error('This is a request to hello')
    return "Hello, World!"

@app.route('/html')
def html():
    return (
        '<div style="background: red">Hello, this a div</div>'
        '<ul>'
        '<li>1</li>'
        '<li>2</li>'
        '<li>3</li>'
        '</ul>'
    )

@app.route('/json')
def my_json():
    return json.dumps({'key': 'value'})

@app.route('/actors')
def get_actors():
    return {'actors': []}, 200

@app.route('/actors/<actor_id>')
def get_id_actors(actor_id):
    app.logger.info(f'Actor id is {actor_id}')
    if actor_id.isalpha():
        app.logger.error(f"Actor id is invalid")
        return f"<div> Actor id is invalid</div>"
    return f"<div> Actor id is {actor_id}</div>", 200

@app.post('/actors')
def create_actor():
    app.logger.info('Actor has been created')
    return 'Creted', 201

# @app.route('/movies', methods=['GET', 'POST'])
# def movies():
#     app.logger.info('movies')
#     return 'ok', 200
@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'GET':
        return "get ok", 200
    elif request.method == 'POST':
        return "post ok", 201
    else:
        return "bed request", 400



@app.route('/movie/<int:movie_id>')
def get_movie(movie_id):
    return f"<div> Movi id is  {movie_id}</div>", 200

@app.route('/movie/<int:movie_id>/actors/<actor_id>')
def get_actor_movie(**kwargs):
    return f"<div> Movi{kwargs.get('movie_id')} Actors{kwargs.get('actor_id')}</div>", 200
# http://localhost:4200/movie/2/actors/546

@app.get('/request-deb')
def request_deb():
    return f'<div>{request.url}</div>'

@app.get('/request-debugger')
def request_debugger():
    res = '<ul>'
    for key, value in request.headers.items():
        res += f'<li>{key} - {value}</li>'
    res += '</ul>'
    return f'<div>{res}</div>'
#
# @app.get('/params-debugger')
# def params_debugger():
#     res = '<ul>'
#     for key, value in request.args.items():
#         res += f'<li>{key} - {value}</li>'
#     res += '</ul>'
#     return f'<div>{res}</div>'
# http://localhost:4200/params-debugger?name=Slava&age=31



@app.get('/params-debugger')
def params_debugger():
    return render_template('/debug.html', attributes=request.args)















# http://localhost:4200/params-debugger?name=Slava&age=31
@app.route('/data-movies', methods=['GET', 'POST'])
def data_movies():
    if request.method == 'GET':
        # print(request.json)
        # print(request.form)
        # виконати запит через постман raw -> json  або form-data відповідно
        html_form = """
        <form method=POST action'/movies'>
            <input type='string' name='movie_name' value"" />
            <input type='password' name='password' value"" />
            <button type='submit'>Send form</button>
        </form>
        """
        return html_form, 200
    elif request.method == 'POST':
        # TODO: записати до бази данних
        return f"movie name {request.form.get('movie_name')}", 201
    else:
        return "bed request", 400

name_list = ['Bob', 'Tony', 'Taras', 'Anna', 'Jane']
book_list = ["The Great Gatsby", "1984", "The Lord of the Rings", "The Hobbit", "Kobzar"]
#
# @app.route('/')
# def start():
#     return "<h1> start </h1>"
#
# @app.route('/hello')
# def hello_world():
#     logging.debug("log DEBUG Message")
#     logging.info("log INFO")
#     logging.warning("log WARNING")
#     logging.error("log ERROR")
#     logging.critical("A message of CRITICAL severity")
#     return 'Hello World!'
#
#
@app.get('/users')
def get_name():
    rand_len = random.randint(1, len(name_list))
    res = random.SystemRandom().sample(name_list, rand_len)
    return render_template('/users.html', res=res)


# @app.get('/params-debugger')
# def params_debugger():
#     return render_template('/debug.html', attributes=request.args)

@app.get('/books')
def get_book():
    res = random.SystemRandom().sample(book_list, random.randint(1, len(book_list)))
    return render_template('/books.html', res=res)
#
#
@app.get('/users/<int:name_id>')
def get_users(name_id):
    print(name_id)
    return render_template('/user_id.html', name_id=name_id)


@app.get('/books_text/<string:title>')
def get_books(title):
    res = title.title()
    return render_template('/books_text.html', res=res)


@app.route('/params')
def html_table_parameters():
    params_dict = request.args.to_dict()
    return render_template('/params.html', item=params_dict.items())


@app.route('/login', methods=['GET', 'POST'])
def reg_form():
    if request.method == 'GET':
        login_form = """
        <form action="/login" method="POST">
          <input type="text" name="username" placeholder="Username"><br>
          <input type="password" name="password" placeholder="Password"><br><br>
          <button type="submit">Submit</button>
        </form>
        """
        return render_template('/login.html', login_form=login_form)
        # return login_form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            abort(400, "Missing username or password")

#
# @app.route('/login', methods=['GET', 'POST'])
# def reg_form():
#     if request.method == 'GET':
#         login_form = """
#         <form action="/login" method="POST">
#           <input type="text" name="username" placeholder="Username"><br>
#           <input type="password" name="password" placeholder="Password"><br><br>
#           <button type="submit">Submit</button>
#         </form>
#         """
#         return login_form
#     elif request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username and password:
#             return redirect('/users')
#         else:
#             abort(400, "Missing username or password")
