
from flask import Flask, render_template, request, redirect
from Ejercicio2_1 import app
from flask_wtf import FlaskForm
from wtforms import SelectField

import Ejercicio2_1.database as database

class RootForm(FlaskForm):
    countries = SelectField('Continentes')

@app.route('/', methods=["GET", "POST"])
def root():
    root_form = RootForm()
    root_form.countries.choices = database.query_continent_name()

    if root_form.validate_on_submit():
        return redirect('/continent/' + root_form.countries.data)

    return render_template("inicio.html", form = root_form)


@app.route('/europe')
def europe_result():
    return render_template("resultado.html", countries = database.query_countries("Europa"))


@app.route('/all')
def all_countries_result():
    return render_template("resultado.html", countries = database.query_countries(""))


@app.route('/without_money')
def without_money():
    return render_template("resultado.html", countries = database.query_without_money_countries())


@app.route('/continent/<string:continent>')
def select_continent(continent):
    return render_template('resultado.html', countries = database.query_countries(continent))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada...")