from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/login')
def login():
    # return 'Hello from app.py!'
    return render_template("login_screen.html")

@app.route('/signUp')
def signUp():
    # return 'Hello from app.py!'
    return render_template("login_screen.html")



# This is the change I made

# @app.route("/", defaults={'path': '/home/'})
# @app.route("/<path:path>")
# def catch_all(path):
#     return render_template("home.html")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/userHomePage")
def userHomePage():
    # route for the user homepage once user logs in
    pass


if __name__ == '__main__':
    app.run(debug=True)
