
from flask import Flask, render_template, request, abort
from Ejercicio2_2 import app

import Ejercicio2_2.database as database


@app.route('/')
def root():
     return render_template("inicio.html")


@app.route('/europe/page/<int:page>')
def europe_result(page):

    pages = database.get_europe_page_count()
    validate_page(page, pages)

    return render_template("resultado.html", url = "europe_result", countries = database.query_countries("Europa", page), pages = pages, page = page)


@app.route('/all/page/<int:page>')
def all_countries_result(page):

    pages = database.get_countries_page_count()
    validate_page(page, pages)

    return render_template("resultado.html", url = "all_countries_result", countries = database.query_countries("", page), pages = pages, page = page)


@app.route('/without_money/page/<int:page>')
def without_money(page):

    pages = database.get_no_money_page_count()
    validate_page(page, pages)

    return render_template("resultado.html", url = "without_money", countries = database.query_without_money_countries(page), pages = pages, page = page)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada...")


def validate_page(page, max_pages):
    if page == 0 or page > max_pages:
        return abort(404)



