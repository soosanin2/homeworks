
from flask import Flask, render_template, redirect, abort
import logging
from .config import AppConfig

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__, template_folder='templates')


app.config.from_object(AppConfig)


from .views import *
from .class_based_views import *


