import logging
import random

from flask import Flask, request, redirect, abort

app = Flask(__name__)


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

@app.route('/hello')
def hello_world():
    logging.debug("log DEBUG Message")
    logging.info("log INFO")
    logging.warning("log WARNING")
    logging.error("log ERROR")
    logging.critical("A message of CRITICAL severity")
    return 'Hello World!'


name_list = ['Bob', 'Tony', 'Taras', 'Anna', 'Jane']
book_list = ["The Great Gatsby", "1984", "The Lord of the Rings", "The Hobbit", "Kobzar"]

@app.get('/users')
def get_name():
    rand_len = random.randint(1, len(name_list))
    return random.SystemRandom().sample(name_list, rand_len)


@app.get('/books')
def get_book():
    res = '<ul>'
    for i in random.SystemRandom().sample(book_list, random.randint(1, len(book_list))):
        res += f'<li>{i}</li>'
    res += '</ul>'
    return f"<div>{res}</div>"


@app.get('/users/<int:name_id>')
def get_users(name_id):
    if name_id % 2 == 0:
        return f'{name_id}', 200
    return f"Not Found", 404


@app.get('/books/<string:title>')
def get_books(title):
    return title.title(), 200


@app.route('/params')
def html_table_parameters():
    params_dict = request.args.to_dict()
    html_table = '<table><tr><th> parameter </th><th> value </th></tr>'
    for key, value in params_dict.items():
        html_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    html_table += '</table>'
    return html_table


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
        return login_form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            abort(400, "Missing username or password")


if __name__ == '__main__':
    app.run()
