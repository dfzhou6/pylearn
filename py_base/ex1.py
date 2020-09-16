# -*- coding: utf-8 -*-

# 多行
s = '''line1
line2
line3
'''
print(s)

# encode,decode
# 代码中的编码类型必须和声名的编码类型一致
# 使用print展示时，必须都已unicode的格式展示
# 对中文进行比较时，必须是以unicode的格式比较
name = u"中文"
name_utf8 = name.encode("utf-8")
name_unicode = name_utf8.decode("utf-8")
print(name_unicode)
print(name)

# format %
f_name = "zdf"
f_age = 24
f_str = "hello i'm %s, i'm %s years old" % (f_name, f_age)
print(f_str)

f2_name = "zdf"
f2_age = 24
f2_str = "hello i'm {}, i'm {} years old".format(f_name, f_age)
print(f2_str)

# set
set_1 = set([1,2,3,4,4,5,5])
print(set_1)

# str 是不可变变量
# list 是可变变量
s_1 = "abc"
s_1_u = s_1.upper()
print(s_1)
print(s_1_u)

l_1 = [1,4,2,3]
l_1.sort()
print(l_1)

# slice 字符串元组也可以
str_s = "abcdefg"
print(str_s[2:])
print(str_s)
t_1 = (1,2,3,4,5)
print(t_1[2:])
print(t_1)

# for list
l_test = list(range(1,11))
print([v*v for v in l_test if v % 2 == 0])

# for str
l_str = "12345"
print([s+"-" for s in l_str])