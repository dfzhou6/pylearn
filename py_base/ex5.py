# -*- coding: utf-8 -*-

# 支持多继承

class Student(object):
    ADDRESS = "Shenzhen"

    def __init__(self, name, score, age):
        self.__name = name # 不能直接被访问，可用特殊方式访问，比如s._Student__name
        self.score = score
        self.__age = age

    def set_score(self, score):
        if 0 < score and score <= 100:
            self.score = score
        else:
            raise ValueError('invalid score')
    
    def get_name(self):
        return self.__name

    @property
    def age(self):
        """
        读属性（切记属性命名不能与方法名相同）
        """
        return self.__age + 1
    
    @age.setter
    def age(self, age):
        """
        写属性
        """
        self.__age += age
        return True
    

s1 = Student("zdf", 59, 20)
print(s1.get_name())
print(s1.score)
s1.set_score(90)
print(s1.score)
# s1.set_score(101)
# print(s1._Student__name)
print(hasattr(s1, "hello"))
setattr(s1, "hello", "okok")
print(getattr(s1, "hello"))
print(s1.hello)
print(Student.ADDRESS)

s1.age = 3
print(s1.age)