# writer:enjoyiii
# 2026年05月15日16时13分51秒
# 15211281589@163.com
import socket
import select
import sys

class ChatServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#端口复用,即使服务器time wait也可以复用
        self.server.bind((self.ip, self.port))
        self.server.listen(10)
        self.epoll= select.epoll()#创建epoll对象

    def chat(self):
        conn,addr=self.server.accept()
        print('connected by', addr)
        self.epoll.register(conn.fileno(), select.EPOLLIN)#注册监控conn
        self.epoll.register(sys.stdin.fileno(), select.EPOLLIN)#注册监控stdin标准输入
        while True:
            events=self.epoll.poll(-1)#返回[(fd,event),()],fd为文件描述符，event为事件,-1表示永久监控
            for fd,event in events:
                if fd==sys.stdin.fileno():
                    data=input()
                    conn.send(data.encode('utf-8'))
                elif fd==conn.fileno():
                    data=conn.recv(1024).decode('utf-8')
                    if data:
                        print(data)
                    else:
                        print('client disconnected')
                        return


if __name__ == '__main__':
    server = ChatServer('127.0.0.1', 8000)
    server.chat()