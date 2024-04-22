# Python standard libraries
import json
import os
import sqlite3

# Third-party libraries
from flask import Flask, redirect, request, url_for, render_template
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
from modules import Modules
from userSelections import UserSelections

# Configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# Flask app setup
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or os.urandom(24)

##
# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# Naive database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/myLearning")
def myLearningPage():
    return "My Learning Page"

@app.route("/saveChecklist", methods=['GET','POST'])
def saveChecklist():
    UserSelections.delete(current_user.id)
    moduleItemIds = request.form.getlist("moduleItemCheckboxInput")
    # print(checklist)
    for moduleItemId in moduleItemIds:
        UserSelections.create(current_user.id, moduleItemId)
    return redirect(url_for("userLogin"))

@app.route("/myProgress")
def myProgressPage():
    return "My Progress Page"

@app.route("/myTodoList", methods=['GET','POST'])
def myTodoListPage():
    if request.method == 'GET':
        return render_template("my_todo_list.html")
    else:
        return render_template("my_todo_list.html")

@app.route("/updateTodoList", methods=['POST'])
def updateTodoListPage():
    id = request.form["taskSelection"]
    # return render_template("my_todo_list.html")
    return f"updateEndpoint {id}"

@app.route("/deleteTodoList", methods=['POST'])
def deleteTodoList():
    id = request.form["taskSelection"]
    return f"deleteEndpoint {id}"

@app.route("/myCommunity")
def myCommunityPage():
    # user = User.getAll(current_user.id)
    # return render_template("community.html", user=user)
    return render_template("community.html")

@app.route("/myProfile")
def myProfilePage():
    user = User.getAllAttributesByUserID(current_user.id)
    return render_template("profilePage.html", user=user)

@app.route("/userDelete", methods=['GET'])
@login_required
def userDelete():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for("userLogin"))

@app.route("/userLogin")
def userLogin():
    if current_user.is_authenticated:
        modules = Modules.getAll()
        userSelctions = UserSelections.getAll(current_user.id)
        # print(userSelctions.ModuleItemID)
        # return "Done"
        return render_template("checklist.html", modules=modules, userSelections=userSelctions)
    else:
        return render_template("login_screen.html")

@app.route("/userUpdate", methods=['GET','POST'])
def userUpdate():
    user = User.getAllAttributesByUserID(current_user.id)
    if request.method == 'GET':
        return render_template("update_profile_screen.html", user=user)
    else:
        user.major = request.form["major"]
        user.year = request.form["year"]
        user.gpa = request.form["gpa"]
        user.advisor = request.form["advisor"]
        user.Enrollment_Status = request.form["Enrollment_Status"]
        user.level = request.form["level"]
        user.program = request.form["program"]
        user.college = request.form["college"]            
        
        User.update(current_user.id, user.major, 
                    user.year, 
                    user.gpa, 
                    user.advisor, 
                    user.Enrollment_Status, 
                    user.level, 
                    user.program, 
                    user.college
                )
        return redirect(url_for("myProfilePage"))

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
    
    # Create a user in your db with the information provided by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    # Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("userLogin"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("userLogin"))


if __name__ == "__main__":
    app.run(ssl_context="adhoc")