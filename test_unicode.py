# -*- coding: utf-8 -*-
# unicode：一套字符集
# utf-8：一套编码
# gbk：一套编码
# 关系：utf-8 === decode(utf-8) ===> unicode ===> encode(gbk) ===> gbk


print(u"你好".encode("utf-8") == "你好")
print(u"你好")
print(repr("你好"))
print(repr(u"你好"))
