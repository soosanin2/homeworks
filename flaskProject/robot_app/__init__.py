
from flask import Flask, render_template, redirect, abort
from flask_sqlalchemy import SQLAlchemy
import logging
from .config import AppConfig


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

db = SQLAlchemy()
app = Flask(__name__, template_folder='templates')

app.config.from_object(AppConfig)

db.init_app(app)

from .views import *
from .class_based_views import *
