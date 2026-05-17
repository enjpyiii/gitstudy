# writer:enjoyiii
# 2026年05月15日22时09分25秒
# 15211281589@163.com
from socket import *
import select
import sys

tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#本地ip地址和端口
tcp_server_socket.bind(('127.0.0.1', 8000))
tcp_server_socket.listen(100)
#设置为非阻塞
tcp_server_socket.setblocking(False)
client_socket = None
while True:
    try:
        client_socket, client_addr = tcp_server_socket.accept()
        print('客户端地址：',client_addr)
    except Exception as e:
        if client_socket:
            data=client_socket.recv(1024)
            if data:
                print('客户端发送的数据：',data.decode('utf-8'))
            else:
                print('客户端断开')
                break
