# -*- coding: utf-8 -*-

from collections import Iterable

# 生成器：为可迭代对象中的一种，另外一种是list,str,tumple,set,dict
# 可使用for访问
def run():
    print("print 1")
    yield 1

    print("print 2")
    yield 2

    print("print 3")
    yield 3

r = run()
print(isinstance(r, Iterable))
print(next(r))
print(next(r))
print(next(r))

for v in run():
    print(v)

# 杨辉三角
def trangle_yang(n):
    if n < 1:
        return

    last = [1]
    yield last

    if n == 1:
        return
    
    for i in range(2, n + 1):
        new_l = []

        for ii in range(i):
            if ii == 0:
                new_l.append(last[ii])
            elif ii > len(last) - 1:
                new_l.append(last[ii - 1])
            else:
                new_l.append(last[ii - 1] + last[ii])

        yield new_l
        last = new_l

for t in trangle_yang(5):
    print(t)


