# writer:enjoyiii
# 2026年05月11日20时55分45秒
# 15211281589@163.com
import socket

#创建udp套接字
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr=('127.0.0.1',8000)#127.0.0.1回环地址表示本机，8000表示监听的端口号
#发送数据
udp_socket.sendto('hello server，我是Windows客户端'.encode('utf-8'),server_addr)

#接收服务器的响应数据
recv_data=udp_socket.recvfrom(1024)
print('接收到的数据是：',recv_data[0].decode('utf-8'))
udp_socket.close()