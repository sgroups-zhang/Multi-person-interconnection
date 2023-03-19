from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from user import *

ip = "127.0.0.1:5000"


@app.route('/')
def inedx():  # put application's code here
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


# @app.route("/new")
# def new_user():
#     return render_template("register.html")
@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        print(1)
        user = request.form['name']
        return redirect(url_for('main', name=user))
    else:
        print(2)
        return render_template("register.html")


@app.route("/user/<name>")
def main(name):
    return render_template("main.html",name=name)


if __name__ == '__main__':
    app.run()
