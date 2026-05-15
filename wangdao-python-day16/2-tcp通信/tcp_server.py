# writer:enjoyiii
# 2026年05月14日19时16分03秒
# 15211281589@163.com
from socket import socket,AF_INET,SOCK_STREAM
import time
#创建套接字，ipv4，tcp
tcp_server = socket(AF_INET, SOCK_STREAM)
#绑定ip和端口
tcp_server.bind(('127.0.0.1', 8000))
#监听连接
tcp_server.listen(5)#有listen才可以别人放数据，（num），num为最大连接数
client_socket, client_addr = tcp_server.accept()#等待客户端连接，三次握手

print('客户端地址：',client_addr)

#接收客户端发送的数据
data = client_socket.recv(1024)
print('客户端发送的数据：',data.decode('utf-8'))

client_socket.send('hello,client.i am tcp_server'.encode('utf-8'))

client_socket.close()#四次挥手
tcp_server.close()#关闭服务器