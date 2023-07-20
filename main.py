import os.path
import sqlite3
from flask import Flask, render_template, url_for, g, request, flash, redirect


DEBUG = True
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/develop')
def develop():
    return render_template("develop.html")

@app.route('/IIdevelop')
def IIdevelop():
    return render_template("IIdevelop.html")

@app.route('/Webdevelop')
def Webdevelop():
    return render_template("Webdevelop.html")

@app.route('/Otzivi')
def Otzivi():
    return render_template("Otzivi.html")

@app.route('/Contacts')
def Contacts():
    return render_template("Contacts.html")

if __name__ == "__main__":
    app.run(debug=True)