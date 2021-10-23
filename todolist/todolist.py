#!/usr/bin/env python

#----------------------------------------------------------------------
# todolist.py
# Authors: Julio Lins
#----------------------------------------------------------------------

from flask import Flask
from flask import render_template, request, redirect
from flask import url_for
import db

#-----------------------------------------------------------------------

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get('add_task')
        author = request.form.get('author')
        db.insert_task(content, author)
        return redirect(url_for('index'))

    for task_id in request.args:
        if task_id.isdigit():
            db.remove_task(task_id)

    tasks = db.get_tasks()
    return render_template('index.html', tasks=tasks)