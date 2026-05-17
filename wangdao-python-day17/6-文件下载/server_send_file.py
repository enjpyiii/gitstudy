# writer:enjoyiii
# 2026年05月15日22时59分20秒
# 15211281589@163.com
import socket
import struct
import os

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_server.bind(('127.0.0.1', 8000))
tcp_server.listen(100)
client_socket, client_addr = tcp_server.accept()

#先发送文件名长度
file_name='test.txt'
file_name_bytes=struct.pack('I',len(file_name.encode('utf-8')))
client_socket.send(file_name_bytes)
#将文件名放在火车车厢发送
client_socket.send(file_name.encode('utf-8'))
#获取文件内容的长度
# file_size=os.stat('test.txt').st_size
file_size=os.path.getsize('test.txt')
#火车头发送文件内容长度
file_size_bytes=struct.pack('I',file_size)
client_socket.send(file_size_bytes)
#火车厢发送文件的内容：可以一次性发完也可以循环发
# client_socket.send('test.txt'.encode('utf-8'))#错误写法



file=open('test.txt','rb')

while True:
    data=file.read(1024)
    if not data:
        break
    client_socket.send(data)
file.close()

tcp_server.close()
client_socket.close()

