from flask import Flask, render_template, url_for, request, redirect

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



# This is the change I made

# @app.route("/", defaults={'path': '/home/'})
# @app.route("/<path:path>")
# def catch_all(path):
#     return render_template("home.html")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/userHomePage", methods=['POST'])
def userHomePage():
    # route for the user homepage once user logs in
    # pass
    username = request.form['username']
    return render_template("userHomePage.html")


if __name__ == '__main__':
    app.run(debug=True)
