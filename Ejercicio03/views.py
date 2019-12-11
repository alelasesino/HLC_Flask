
from flask import Flask, render_template, request, redirect, url_for, abort
from Ejercicio03 import app
from Ejercicio03.task_form import TaskForm
from Ejercicio03.models import Task

import Ejercicio03.database as database

@app.route('/')
def root():
    return render_template("inicio.html")


@app.route('/task/add', methods=['GET', 'POST'])
def add_task():

    form = TaskForm()
    
    if form.validate_on_submit():
        
        task = Task(-1, form.fecha.data, form.descripcion.data, form.prioridad.data, form.estado.data)
        database.insert_task(task)

        return redirect(url_for('root'))

    else:
        return render_template("task_form.html", form = form, post_url = 'add_task')


@app.route('/task/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):

    form = TaskForm()

    bind_data_task_form(form, database.get_task_by_id(task_id))

    if form.validate_on_submit():

        task = Task(-1, form.fecha.data, form.descripcion.data, form.prioridad.data, form.estado.data)
        database.insert_task(task)

        return redirect(url_for('root'))

    else:
        return render_template("task_form.html", form = form, post_url = 'update_task', task_id = 1)


def bind_data_task_form(form, task):

    if(task == None):
        abort(404)

    form.fecha.data = task.fecha
    form.descripcion.data = task.descripcion
    form.prioridad.data = task.prioridad
    form.estado.data = task.estado
        

"""
@app.route('/task/remove/<int:task_id>')
def all_countries_result():
    return render_template("task_form.html", form = database.query_countries(""))
"""

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada...")