
from flask import Flask, render_template, request
from Ejercicio01 import app

import Ejercicio01.database as database


@app.route('/')
def root():
    return render_template("inicio.html")


@app.route('/europe')
def europe_result():
    return render_template("resultado.html", countries = database.query_countries("Europa"))


@app.route('/all')
def all_countries_result():
    return render_template("resultado.html", countries = database.query_countries(""))


@app.route('/without_money')
def without_money():
    return render_template("resultado.html", countries = database.query_without_money_countries())


#@app.errorhandler(404)
#def page_not_found(error):
#    return render_template("error.html", error="Página no encontrada..."), 404