# writer:enjoyiii
# 2026年05月15日22时59分32秒
# 15211281589@163.com
from socket import *
import select
import sys
import time
import struct

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(('127.0.0.1', 8000))


#接受文件名
filename_len=tcp_client.recv(4)
file_name=tcp_client.recv(struct.unpack('I',filename_len)[0])#接收文件名长度
print('文件名：',file_name.decode('utf-8'))
# file=open(file_name.decode('utf-8'),'wb')
file=open('test1.txt','wb')

file_len=struct.unpack('I',tcp_client.recv(4))[0]
print('文件大小：',file_len)
# data=tcp_client.recv(file_len)#错误写法
# file.write(data)
total=0
while total<file_len:
    text_bytes=tcp_client.recv(10)
    total+=len(text_bytes)
    print('已接收：',total)
    file.write(text_bytes)

file.close()
tcp_client.close()