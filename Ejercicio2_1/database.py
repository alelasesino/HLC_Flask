
import mysql.connector
from contextlib import closing

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="paises"
)


def query_continent_name():

    with closing(db.cursor()) as c:

        c.execute("SELECT continente FROM paises GROUP BY continente HAVING continente IS NOT NULL ORDER BY continente")

        registros = c.fetchall()
        result = []
        
        for nombre in registros:
            result.append((nombre[0], nombre[0]))
        
        return result


def query_countries(continent):

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