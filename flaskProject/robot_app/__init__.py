
from flask import Flask, render_template, redirect, abort
import logging
from .config import AppConfig
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

db = SQLAlchemy()
app = Flask(__name__, template_folder='templates')

app.config.from_object(AppConfig)

db.init_app(app)

from .views import *
from .models import *

with app.app_context():
    db.create_all()
