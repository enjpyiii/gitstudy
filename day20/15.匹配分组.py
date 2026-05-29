# writer:enjoyiii
# 2026年05月29日20时14分35秒
# @163.com
import re

ret=re.match(r"[1-9]?\d$|100","100")
if ret:
    print(ret.group())
else:
    print("匹配失败")



ret = re.match(r"\w{4,20}@(163|126|qq)\.com","test@126.com")#不能将括号去掉，否则意思完全不同
print(ret.group())#test@126.com

ret = re.match(r"\w{4,20}@(163|126|qq)\.com","test@qq.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、q9 邮箱") # 不是163、126、qq 邮箱

ret = re.match(r"\w{4,20}@(163|126|qq)\.com","test@gmail.com")
if ret:
    print(ret.group())
else:
    print("不是163、126、q9 邮箱") # 不是163、126、qq 邮箱

ret =re.match(r"([^-]+)-(\d+)","010-12345678")#没有遇到-之前就一直吃
if ret:
    print(ret.group())
    print(ret.group(1))
    print(ret.group(2))
else:
    print("匹配失败")

print("-----------------")
#学习引用分组
#能够完成对正确的字符串的匹配
ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>","<html>hh</html>")
print(ret.group())
# 如果遇到非正常的 htm1 格式字符串，匹配出错
ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>","<html>hh</htmlbalabala>")
print(ret.group())
#正确写法
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>","<html>hh</htmlbalabala>")#\1:要和第一组一摸一样
if ret:
    print(ret.group())
else:
    print("匹配失败")
print("-----------------")
#匹配多个分组
labels =["<html><h1>www.cskaoyan.com</h1></html>","<html><h1>www.cskaoyan.com</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",label)
    if ret:
        print("%s 是符合要求的标签"% ret.group())
    else:
        print("%s 不符合要求"% label)

print("-----------------")
ret =re.match (r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>","<html><h1>www.cskaoyan.com</h2></html>")
if ret:
    print("%s 是符合要求的标签"% ret.group())
else:
    print("不符合要求")