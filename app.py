from flask import Flask, render_template, request, redirect, url_for, make_response
from apps import create_app

# from flask_script import Manager
# app = Flask(__name__,template_folder="/templates")
app = create_app()
# manager = Manager(app=app)
#
ip = "127.0.0.1:5000"


@app.route('/')
def inedx():  # put application's code here
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/set_cookies/<a>/<b>/")
def set_cookie(a, b):
    resp = make_response("success")
    resp.set_cookie(a, b, max_age=7000)
    return resp


@app.route("/get_cookies/<name>")
def get_cookie(name):
    cookie_1 = request.cookies.get(name)  # 获取名字为Itcast_1对应cookie的值
    return cookie_1


@app.route("/delete_cookies/<name>")
def delete_cookie(name):
    resp = make_response("del success")
    resp.delete_cookie(name)

    return resp


if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/new")
# def new_user():
#     return render_template("register.html")
# @app.route('/register/', methods=['POST', 'GET'])
# def register():
#     if request.method == 'POST':
#         print(1)
#         user = request.form['name']
#         return redirect(url_for('main', name=user))
#     else:
#         print(2)
#         return render_template("register.html")


# @app.route("/user/<name>/")
# def main(name):
#     return render_template("main.html",name=name)


# if __name__ == '__main__':
#     app.run()
