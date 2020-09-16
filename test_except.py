# -*- coding: utf-8 -*-

def check_file(filename):
    try:
        with open(filename):
            pass
    except Exception:
        print(filename + " is not found")
    else:
        print(filename + " is found")

files = ["function.py", "hello.py", "zdf.py"]
for filename in files:
    check_file(filename)