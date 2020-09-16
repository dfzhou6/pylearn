# -*- coding: utf-8 -*-

import json
import time


class Login(object):

    def __init__(self):
        self.filename = "username.json"
        self.user_info = {}
        self.init_user_info()

    def init_user_info(self):
        try:
            with open(self.filename) as file_obj:
                self.user_info = json.load(file_obj)
        except Exception:
            return {}
        finally:
            return {}

    def do_login(self, username):
        user_info = self.read_username(username)
        if user_info:
            print("welcome " + username + ", create_time is " + str(user_info["create_time"]))
        else:
            self.regist_username(username)

    def read_username(self, username):
        return self.user_info[username] if username in self.user_info else {}

    def regist_username(self, username):
        with open(self.filename, "w") as file_obj:
            self.user_info[username] = {
                "name": username,
                "create_time": int(time.time())
            }
            json.dump(self.user_info, file_obj)
            print(username + " regist succeed")

l = Login()
l.do_login(u"关羽")
l.do_login(u"张飞")

data = {
    "name": u"周",
    "age": 24
}
json_str = json.dumps(data)
print(json_str)
ret = json.loads(json_str)
print(ret)
print(ret["name"])
