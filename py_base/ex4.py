# -*- coding: utf-8 -*-

# decorater装饰器
# wraps作用是保持被调用的方法名称不变，即func.__name__

from functools import wraps

def hello(func):
    @wraps(func)
    def wrapper(*tu, **dt):
        print("hello before")
        func(*tu, **dt)
        print("hello after")
    return wrapper

def hi(text):
    def deco(func):
        @wraps(func)
        def wrapper(*tu, **dt):
            print("hello before " + text)
            func(*tu, **dt)
            print("hello after " + text)
        return wrapper
    return deco

@hi("okok")
def running(name, age):
    print(name + " age is " + str(age) + ", running every day")


running("zdf", 24)

