# -*- coding: utf-8 -*-

"""
枚举类
"""
from enum import Enum

class Toy(Enum):
    Bear = 1
    Car = 2
    Dog = 3

for name, member in Toy.__members__.items():
    print("{} {} {}".format(name, member, member.value))

print(Toy.Dog.value)
print(Toy(3))
