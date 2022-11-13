from app import app
from flask import render_template, redirect, url_for, flash, request, session


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Clinica veterinară Sandu")


@app.route('/echipa')
def echipa():
    return render_template("echipa.html", title="Clinica veterinară Sandu - Echipa")


@app.route('/tarife_servicii')
def tarife_servicii():
    return render_template("tarife_servicii.html", title="Clinica veterinară Sandu - Tarife & Servicii")