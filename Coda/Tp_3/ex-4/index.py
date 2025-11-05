from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/traitement", methods=["POST"])
def traitement():
    traductions = {
        "mot": "word",
        "supprimer": "remove",
        "requête": "request",
        "méthode": "method",
        "répertoire": "directory",
    }
    traduction2 = {
        "word": "mot",
        "remove": "supprimer",
        "request": "requête",
        "method": "méthode",
        "directory": "répertoire",
    }

    donnees = request.form
    word = donnees.get("word").lower()
    trad = donnees.get("direction").lower()
    result = None

    if trad == "fr-en" and word in traductions:
        result = traductions[word]
    elif trad == "en-fr" and word in traduction2:
        result = traduction2[word]
    else:
        result = "erreur"
        return render_template("traitement.html", result=result)

    return render_template("traitement.html", trad=trad, word=word, result=result)
