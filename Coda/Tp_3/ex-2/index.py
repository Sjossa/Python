from flask import Flask, render_template
import random


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/loto")
def loto():

    resultat = random.sample(range(1, 50), 6)
    return render_template("index.html", resultat=resultat)


@app.route("/livre")
def livre():
    books = [
        {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "category": "Informatique",
            "stock": 3,
        },
        {
            "title": "Le Crime de l'Orient-Express",
            "author": "Agatha Christie",
            "category": "Mystère",
            "stock": 4,
        },
        {
            "title": "Les Misérables",
            "author": "Victor Hugo",
            "category": "Roman",
            "stock": 1,
        },
        {
            "title": "Steve Jobs",
            "author": "Walter Isaacson",
            "category": "Biographie",
            "stock": 0,
        },
    ]

    return render_template("livre.html", books=books)
