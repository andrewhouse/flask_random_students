from os import path
from flask import render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, IntegerField, SubmitField

from app.lib.random_groups import RandomGroups
from app import app

class PerGroupForm(Form):
    per_group = IntegerField('Per Group:', validators=[validators.required()])

#Index Route
@app.route("/", methods=['GET', 'POST'])
def index():
    form = PerGroupForm(request.form)
    if request.method == 'POST':
        per_group = form.data['per_group'] or 2
        groups = RandomGroups(per_group)
    else:
        groups = RandomGroups()
    return render_template('index.html', groups=groups.teams, form=form)

