
import math
import mysql.connector
from contextlib import closing

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="paises"
)


PERPAGE = 20


def query_countries(continent, page):

    start_page = get_start_page(page)
    
    with closing(db.cursor()) as c:

        if continent != "":

            sql_query = "SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE continente = %s ORDER BY nombre LIMIT %s, %s"
            c.execute(sql_query, [continent, start_page, PERPAGE])

        else:

            c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises ORDER BY nombre LIMIT %s, %s", (start_page, PERPAGE))

        return c.fetchall()


def query_without_money_countries(page):
    
    start_page = get_start_page(page)

    with closing(db.cursor()) as c:

        c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE iso_moneda IS NULL ORDER BY nombre LIMIT %s, %s", (start_page, PERPAGE))

        return c.fetchall();


def get_start_page(page):
    return (page-1) * PERPAGE


def get_countries_page_count():
    return count_query_rows("SELECT COUNT(*) AS 'rows' FROM paises ORDER BY nombre")


def get_europe_page_count():
    return count_query_rows("SELECT COUNT(*) AS 'rows' FROM paises WHERE continente = 'Europa' ORDER BY nombre")


def get_no_money_page_count():
    return count_query_rows("SELECT COUNT(*) AS 'rows' FROM paises WHERE iso_moneda IS NULL ORDER BY nombre");


def count_query_rows(query):

    with closing(db.cursor(dictionary=True)) as c:

        c.execute(query)
        
        pages = c.fetchone()["rows"] / PERPAGE
        
        return int(math.ceil(pages));
    
