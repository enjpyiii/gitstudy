# writer:enjoyiii
# 2026年05月28日23时42分26秒
# @163.com
import re

ret=re.match("[A-Z][a-z]*","M")
print(ret.group())

ret=re.match("[A-Z][a-z]*","MnnM")
print(ret.group())

ret=re.match("[A-Z][a-z]*","Abcdef")
print(ret.group())

print("-----------------")
names=["name1","_name","2_name","__name__"]
for name in names:
    ret=re.match(r"[a-zA-Z]+[\w]*",name)
    if ret:
        print(ret.group())
    else:
        print("匹配失败")

print("-----------------")

ret=re.match(r"[1-9]?[0-9]","7")
print(ret.group())

ret=re.match(r"[1-9]?\d","33")
print(ret.group())

ret=re.match(r"[1-9]?\d","09")
print(ret.group())
print("-----------------")
#匹配1-99之间的数字
ret=re.match(r"[1-9]?\d$","09")
if ret:
    print(ret.group())
else:
    print("匹配失败")

ret=re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())

ret=re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())