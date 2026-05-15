# writer:enjoyiii
# 2026年05月14日19时15分47秒
# 15211281589@163.com
from socket import socket,AF_INET,SOCK_STREAM
import time
#创建套接字，ipv4，tcp
tcp_client = socket(AF_INET, SOCK_STREAM)

#连接服务器
tcp_client.connect(('127.0.0.1', 8000))

#发送数据
tcp_client.send('我是TCP客户端'.encode('utf-8'))
#接收数据
data = tcp_client.recv(1024)
print('服务端发送的数据：',data.decode('utf-8'))

#关闭
tcp_client.close()