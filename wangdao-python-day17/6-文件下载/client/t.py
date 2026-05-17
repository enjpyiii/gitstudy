# writer:enjoyiii
# 2026年05月16日15时26分58秒
# 15211281589@163.com
import os
file=open('test1.txt','r')
data=file.read()
print(os.path.abspath('test1.txt'))
print( data)
file.close()