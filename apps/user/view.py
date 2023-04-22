import json
import os

from flask import Blueprint, request, redirect, render_template, url_for, make_response

user_bp = Blueprint("user", __name__)  # 创建蓝图


@user_bp.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        print(1)
        user = request.form['name']
        if request.form["password"] == request.form["confirm"]:
            password = request.form['password']
        else:
            return render_template("error.html", info="密码不一致！")
        with open("data/users/user_list.json", "r", encoding="utf-8") as f:
            info = json.load(f)
            info = info["users"]
            if user in info:
                return render_template("error.html", info="用户已存在")
        os.mkdir("data/users/" + user)
        with open("data/users/user_list.json", "w", encoding="utf-8") as f:
            info.append(user)
            json.dump({"users": info}, f)
        with open("data/users/{}/info.json".format(user), "w", encoding="utf-8") as fp:
            data = {
                "info": {
                    "name": user,
                    "password": password
                }
            }
            json.dump(data, fp)
        resp = make_response(redirect(url_for('user.main', name=user)))
        resp.set_cookie("login", user, max_age=991800)
        return resp
    else:
        try:
            cookie_1 = request.cookies.get("login")
            print(cookie_1)
        except TypeError:
            return render_template("register.html")
        if cookie_1 == "false" or cookie_1 is None:
            return render_template("register.html")

        print(2)
        return render_template("main.html", name=cookie_1)


@user_bp.route("/user/<name>/")
def main(name):
    return render_template("main.html", name=name)
