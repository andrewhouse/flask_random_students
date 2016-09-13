from os import path
from flask import render_template

from app import app
from app.lib.random_groups import RandomGroups

@app.route("/")
def index():
    return render_template('index.html')

