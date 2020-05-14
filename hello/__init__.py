from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def root():
    from . import models

    models.Log.add_entry()
    return "<html><h1>Hello World !</h1></html>"


@app.route("/logs")
def logs():
    from . import models

    entries = models.Log.get_entries()
    entries = map(lambda e: e[0].strftime("%d/%m/%Y %H:%M:%S"), entries)
    entries = map(lambda e: f"<p>{e}</p>", entries)
    entries = "\n".join(entries)
    return f"<html>{entries}</html>"
