# -*- coding: utf-8 -*-

"""
__getattribute__
__str__
__call__
"""

class Test(object):
    def __getattribute__(self, attr):
        if attr == "name":
            return "yes name"
    
    def __str__(self):
        return "test str"

    def __call__(self):
        return "call by yourself"
        
t = Test()
print(t.name)
print(t.name2)
print(t())
print(t)
print(callable(t))
