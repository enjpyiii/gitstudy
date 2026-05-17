# writer:enjoyiii
# 2026年05月15日22时30分32秒
# 15211281589@163.com
import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server.bind(('127.0.0.1', 8000))
tcp_server.listen(100)
client_socket, client_addr = tcp_server.accept()
print('客户端地址：',client_addr)

while True:
    pass