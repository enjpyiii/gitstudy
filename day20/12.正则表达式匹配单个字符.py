# writer:enjoyiii
# 2026年05月25日23时45分24秒
# @163.com
import re
result=re.match('wangdao','wangdao.cn')
print(result.group())

ret=re.match(".","M")
print(ret.group())
ret=re.match("t.o","too")
print(ret.group())
ret=re.match("t.o","two")
print(ret.group())

#大小写h都可以的情况
ret=re.match("[Hh]","hello")
print(ret.group())
ret=re.match("[Hh]el","Hello")
print(ret.group())
# ret=re.match("[Hh]ello","Hell")#会报错
# print(ret.group())
ret=re.match("[0-35-9]ello","4ello")
if ret:
    print('yes')
else:
    print("匹配失败")

ret=re.match(r"嫦娥\d号","嫦娥1号")#\d表示数字,不加r会有语法警告
print(ret.group())
ret=re.match(r"嫦娥\d号","嫦娥10号")
if ret:
    print('yes')
else:
    print("匹配失败")