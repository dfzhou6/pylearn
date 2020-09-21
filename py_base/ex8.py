# -*- coding: utf-8 -*-

"""
元类：type metaclass
用来定义类的类，可以理解为平时的类可通过元类来定义
元类 => 类 => 实例
"""

class TestMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add_attr"] = lambda self, value: setattr(self, value, 1)
        return type.__new__(cls, name, bases, attrs)


class Hello(object):
    __metaclass__ = TestMetaclass

h = Hello()
h.add_attr("okok")
h.add_attr("sdsd")
print(h.okok)
print(h.sdsd)
