
from flask import Flask, render_template, request, redirect, url_for, abort
from Ejercicio03 import app
from Ejercicio03.forms import TaskForm, SelectTaskForm, TaskListForm
from Ejercicio03.models import Task

import Ejercicio03.database as database

@app.route('/')
def root():
    return render_template("inicio.html", message = "Crea, modifica y elimina las tareas de tu agenda.")


@app.route('/task/add', methods=['GET', 'POST'])
def add_task():

    form = TaskForm(False)
    
    if form.validate_on_submit():
        
        task = Task(-1, form.fecha.data, form.descripcion.data, form.prioridad.data, form.estado.data)
        database.insert_task(task)

        return render_template("inicio.html", message = "Tareas creada correctamente.")
        #return redirect(url_for('root'))

    else:
        return render_template("task_form.html", form = form, post_url = 'add_task')


@app.route('/task/update', methods=['GET', 'POST'])
def select_update_task():

    task_list = database.get_all_task()

    form = SelectTaskForm(task_list)

    if form.validate_on_submit():
        return redirect(url_for('update_task', task_id = form.id.data))

    else:
        return render_template("select_task.html", operation = "actualizar", 
                                                   task_list = task_list, 
                                                   form = form, 
                                                   post_url = 'select_update_task')


@app.route('/task/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):

    form = TaskForm(True)

    if not form.is_submitted():
        bind_data_task_form(form, database.get_task_by_id(task_id))

    if form.validate_on_submit():
        task = Task(task_id, form.fecha.data, form.descripcion.data, form.prioridad.data, form.estado.data)
        database.update_task(task)

        #return redirect(url_for('root'))
        return render_template("inicio.html", message = "Tarea modifica correctamente.")

    else:
        return render_template("task_form.html", form = form, post_url = 'update_task', task_id = task_id)


@app.route('/task/delete', methods=['GET', 'POST'])
def select_delete_task():

    task_list = database.get_all_task()

    form = SelectTaskForm(task_list)

    if form.validate_on_submit():
        delete_task(form.id.data)
        #return redirect(url_for('root'))
        return render_template("inicio.html", message = "Tarea borrada correctamente.")

    else:
        return render_template("select_task.html", operation = "borrar", 
                                                   task_list = task_list, 
                                                   form = form, 
                                                   post_url = 'select_delete_task')


#@app.route('/task/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    database.delete_task(task_id)


def bind_data_task_form(form, task):
    
    if(task == None):
        abort(404)

    form.fecha.data = task.fecha
    form.descripcion.data = task.descripcion
    form.prioridad.data = task.prioridad
    form.estado.data = task.estado


@app.route('/task/list', methods=['GET'])
def task_list():

    task_list = database.get_all_task()

    form = TaskListForm()

    return render_template("task_list.html", title = "Lista de tareas", form = form, task_list = task_list)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada...")