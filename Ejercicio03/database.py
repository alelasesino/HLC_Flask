
import mysql.connector
from contextlib import closing
from Ejercicio03.models import Task

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="paises"
)


def get_all_task():

    with closing(db.cursor()) as c:

        sql_query = "SELECT id, fecha, descripcion, prioridad, estado FROM agenda"
        c.execute(sql_query)

        tasks = []

        for (id, fecha, descripcion, prioridad, estado) in c:
            tasks.append(Task(id, fecha, descripcion, prioridad, estado))

    return tasks


def get_state_task(state):

    with closing(db.cursor()) as c:

        sql_query = "SELECT id, fecha, descripcion, prioridad, estado FROM agenda WHERE estado = %s"
        c.execute(sql_query, [state])

        tasks = []

        for (id, fecha, descripcion, prioridad, estado) in c:
            tasks.append(Task(id, fecha, descripcion, prioridad, estado))

    return tasks


def get_priority_task(priority):

    with closing(db.cursor()) as c:

        sql_query = "SELECT id, fecha, descripcion, prioridad, estado FROM agenda WHERE prioridad = %s"
        c.execute(sql_query, [priority])

        tasks = []

        for (id, fecha, descripcion, prioridad, estado) in c:
            tasks.append(Task(id, fecha, descripcion, prioridad, estado))

    return tasks


def get_task_by_id(task_id):

    with closing(db.cursor()) as c:

        sql_query = "SELECT id, fecha, descripcion, prioridad, estado FROM agenda WHERE id = %s"
        c.execute(sql_query, [task_id])
        
        result = c.fetchone()

        if result != None:
            (id, fecha, descripcion, prioridad, estado) = result

            return Task(id, fecha, descripcion, prioridad, estado)


def insert_task(task):

    with closing(db.cursor()) as c:

        sql_query = "INSERT INTO agenda(fecha, descripcion, prioridad, estado) VALUES(%s, %s, %s, %s)"
        c.execute(sql_query, (task.fecha, task.descripcion, task.prioridad, task.estado))
        db.commit()


def delete_task(task_id):

    with closing(db.cursor()) as c:
        
        sql_query = "DELETE FROM agenda WHERE id = %s"
        c.execute(sql_query, [task_id])
        db.commit()


def update_task(task):

    with closing(db.cursor()) as c:
        
        sql_query = "UPDATE agenda SET fecha = %s, descripcion = %s, prioridad = %s, estado = %s WHERE id = %s"
        c.execute(sql_query, (task.fecha, task.descripcion, task.prioridad, task.estado, task.id))
        db.commit()

"""

def query_without_money_countries():
    
    with closing(db.cursor()) as c:

        c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE iso_moneda IS NULL ORDER BY nombre")

        return c.fetchall();

"""