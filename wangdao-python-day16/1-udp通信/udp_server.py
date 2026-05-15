# writer:enjoyiii
# 2026年05月11日21时01分21秒
# 15211281589@163.com
import socket

#创建socket对象，使用IPV4和UDP
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定ip和端口
udp_server.bind(('127.0.0.1', 8000))
#接收数据，最大接受数据量为1024字节
recv_data=udp_server.recvfrom(1024)
#打印接受到的数据
print(recv_data[0].decode('utf-8'))
#打印发送数据的ip和端口
print(recv_data[1])
#发送数据给客户端
udp_server.sendto(b'hello client,i am UDP server',recv_data[1])
#关闭套接字
udp_server.close()