from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from app.py!'


# This is the change I made

@app.route("/home/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
