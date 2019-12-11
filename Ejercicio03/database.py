
import mysql.connector
from contextlib import closing
from Ejercicio03.models import Task

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="paises"
)

def get_task_by_id(task_id):

    with closing(db.cursor()) as c:

        sql_query = "SELECT id, fecha, descripcion, prioridad, estado FROM agenda WHERE id = %s"
        c.execute(sql_query, [task_id])

        for (id, fecha, descripcion, prioridad, estado) in c:
            return Task(id, fecha, descripcion, prioridad, estado)
            

def insert_task(task):

    with closing(db.cursor()) as c:

        sql_query = "INSERT INTO agenda(fecha, descripcion, prioridad, estado) VALUES(%s, %s, %s, %s)"
        c.execute(sql_query, (task.fecha, task.descripcion, task.prioridad, task.estado))
        db.commit()

"""
def update_task(task):

    with closing(db.cursor()) as c:

        if continent != "":

            sql_query = "SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE continente = %s ORDER BY nombre"
            c.execute(sql_query, [continent])

        else:

            c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises ORDER BY nombre")

        return c.fetchall()


def query_without_money_countries():
    
    with closing(db.cursor()) as c:

        c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE iso_moneda IS NULL ORDER BY nombre")

        return c.fetchall();

"""