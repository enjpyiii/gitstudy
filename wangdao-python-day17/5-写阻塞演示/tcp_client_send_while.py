# writer:enjoyiii
# 2026年05月15日22时30分50秒
# 15211281589@163.com
import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('127.0.0.1', 8000))

data='1'*1000
total_len=0
while True:
    data_len=tcp_client.send(data.encode('utf-8'))#send是有返回值的
    total_len+=data_len
    print('发送了：字节',total_len)
