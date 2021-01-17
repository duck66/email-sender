from app import app

from flask import render_template, request, redirect

from app.controllers.emails import save_emails

@app.route("/")
def index():
    return "Let's see if it work"


@app.route("/save_email", methods=["GET",])
def emails():
    return render_template("index.html")
