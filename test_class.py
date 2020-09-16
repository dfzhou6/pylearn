# -*- coding: utf-8 -*-

class Dog(object):

    def __init__(self, name = "default"):
        self.name = name
        print("Dog init...")
        print("Dog name is " + self.name)

    def run(self):
        print("Dog run")


dog = Dog()
dog.run()


class Husky(Dog):

    def __init__(self, name = "default"):
        super(Husky, self).__init__(name)

    def run(self):
        super(Husky, self).run()
        print("Husky run")

hu = Husky("Soso")
hu.run()

from collections import OrderedDict
od = OrderedDict()
od["Mike"] = "Python"
od["Jack"] = "Go"
od["Amy"] = "C++"

for k, v in od.items():
    print(str(k) + "'s favorite lang is " + str(v))