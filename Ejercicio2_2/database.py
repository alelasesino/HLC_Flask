
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
    """Obtiene los paises del contiente deseado
    
    Arguments:
        continent {str} -- Continente al que pertenecen los paises
        page {int} -- Pagina a mostrar
    
    Returns:
        array tuples -- (NOMBRE, ISO3, CONTINENTE, MONEDA)
    """
    start_page = get_start_page(page)
    
    with closing(db.cursor()) as c:

        if continent != "":

            sql_query = "SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE continente = %s ORDER BY nombre LIMIT %s, %s"
            c.execute(sql_query, [continent, start_page, PERPAGE])

        else:

            c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises ORDER BY nombre LIMIT %s, %s", (start_page, PERPAGE))

        return c.fetchall()


def query_without_money_countries(page):
    """Obtiene los paises que no tienen moneda de la pagina deseada
    
    Arguments:
        page {int} -- Pagina a mostrar
    
    Returns:
        tuple -- (NOMBRE, ISO3, CONTINENTE, MONEDA)
    """
    start_page = get_start_page(page)

    with closing(db.cursor()) as c:

        c.execute("SELECT nombre, iso3, continente, nombre_moneda FROM paises WHERE iso_moneda IS NULL ORDER BY nombre LIMIT %s, %s", (start_page, PERPAGE))

        return c.fetchall();


def get_start_page(page):
    """Obtiene el numero del registro por el que debe empezar la pagina
    
    Arguments:
        page {int} -- Pagina a mostrar
    
    Returns:
        int -- Numero del registro inicial
    """
    return (page-1) * PERPAGE


def get_countries_page_count():
    """Obtiene el numero de paginas de todos los paises
    
    Returns:
        int -- Numero de paginas
    """
    return count_query_rows("SELECT COUNT(*) AS 'rows' FROM paises ORDER BY nombre")


def get_europe_page_count():
    """Obtiene el numero de paginas de todos los paises de europa
    
    Returns:
        int -- Numero de paginas
    """
    return count_query_rows("SELECT COUNT(*) AS 'rows' FROM paises WHERE continente = 'Europa' ORDER BY nombre")


def get_no_money_page_count():
    """Obtiene el numero de paginas de todos los paises que no tienen moneda
    
    Returns:
        int -- Numero de paginas
    """
    return count_query_rows("SELECT COUNT(*) AS 'rows' FROM paises WHERE iso_moneda IS NULL ORDER BY nombre");


def count_query_rows(query):
    """Obtiene el numero de registros de la consulta y obtiene el numero de paginas
    necesarias para ese numero de registros
    
    Arguments:
        query {str} -- Consulta SQL con una columna llamada 'rows'
    
    Returns:
        int -- Numero de paginas
    """
    with closing(db.cursor(dictionary=True)) as c:

        c.execute(query)
        
        pages = c.fetchone()["rows"] / PERPAGE
        
        return int(math.ceil(pages));
    
