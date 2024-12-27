from flask import render_template
from . import db
from .models import Tour

def index():
    tours = Tour.query.all()
    return render_template("index.html", tours=tours)