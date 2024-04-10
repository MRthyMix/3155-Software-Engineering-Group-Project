import json
import os
import sqlite3

from flask import Flask, render_template, url_for, request, redirect



from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from db import init_db_command
from user import User

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login_screen.html")
    else:
        username = request.form['username']
        password = request.form['password']
        return render_template("userHomePage.html")


@app.route('/signUp', methods=['POST'])
def signUp():
    fullname = request.form['fullname']
    return render_template("userHomePage.html", name=fullname)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/userHomePage", methods=['POST', 'GET'])
def userHomePage():
    # route for the user homepage once user logs in
    # pass
    # username = request.form['username']
    return render_template("checklist.html")


if __name__ == '__main__':
    app.run(debug=True)
