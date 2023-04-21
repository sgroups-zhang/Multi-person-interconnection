from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, index=True)

    def __init__(self):
        pass
    def check_info(self,name,phone,password,check_password):
        if len(name) > 20:
            return "用户名不能大于20个字符"
        if len(phone) != 11:
            return "手机号长度不是11位数"
        if password != check_password:
            return "前后密码不一致"

