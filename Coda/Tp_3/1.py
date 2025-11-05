from flask import Flask, request
import random

app = Flask(__name__)


@app.route("/loto")
def loto():

    resultat = random.sample(range(1, 50), 6)
    return f"{resultat}"


@app.route("/loto/carre")
def carre():

    contenue = request.args.get("nombre")
    contenue = int(contenue)

    total = contenue**2

    return f"{total}"
