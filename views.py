from flask import Flask, render_template, request, redirect, session, jsonify
from model import bdd

# from .model import bdd as bdd
# from werkzeug.utils import secure_filename
# import pandas, os
# from openpyxl import Workbook

app = Flask(__name__)

app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('MyApp.config')

# page authentification
@app.route("/")
def index(): 
    return render_template("index.html")

# page about us
@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

# Rappels contacts
@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/WEBMASTERS")
def cWEBMASTERS():
    return render_template("WEBMASTERS.html")

@app.route("/SM1")
def SM1():
    return render_template("about-us.html")

@app.route("/SM2")
def SM2():
    return render_template("about-us.html")

@app.route("/Se connecter")
def Se_connecter():
    return render_template("Se connecter.html")

@app.route("/Logout")
def logout():
    session.clear()
    return redirect("/Se connecter/logoutOK")

#page sgbd
@app.route("/sgbd")
def sgbd():
    listeMembres = bdd.get_membresData()
    params ={
    'liste':listeMembres
    }
    params = f.messageInfo(params)
    return render_template("sgbd.html", **params)


# authentification
@app.route("/connecter", methods=["POST"])
def connect():
    login = request.form['login']
    mdp = request.form['mdp']
    user = bdd.verifAuthData(login, mdp)
    print(user)
    try:
    # Authentification réussie
        session["idUser"] = user["idUser"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["mail"] = user["mail"]
        session["statut"] = user["statut"]
        session["avatar"] = user["avatar"]
        session["infoVert"]="Authentification réussie"
        return redirect("/")
    except TypeError as err:
# Authentification refusée
        session["infoRouge"]="Authentification refusée"
        159
        return redirect("/login")