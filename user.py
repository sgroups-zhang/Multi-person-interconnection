class User():
    def __init__(self):
        pass
    def check_info(self,phone,password,check_password):
        if len(phone) != 11:
            return "手机号长度不是11位数"
        if password != check_password:
            return "前后密码不一致"
