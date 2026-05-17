# writer:enjoyiii
# 2026年05月15日16时13分25秒
# 15211281589@163.com
import socket
import select
import sys

class ChatClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))
        self.epoll = select.epoll()

    def chat_client(self):
        self.epoll.register(sys.stdin.fileno(), select.EPOLLIN)
        self.epoll.register(self.client.fileno(), select.EPOLLIN)
        while True:
            events = self.epoll.poll()
            for fd, event in events:
                if fd == self.client.fileno():
                    data = self.client.recv(1024)
                    if not data:
                        print('server disconnected')
                        return
                    print(data.decode('utf-8'))
                elif fd == sys.stdin.fileno():
                    data = input()
                    self.client.send(data.encode('utf-8'))


if __name__ == '__main__':
    client = ChatClient('127.0.0.1', 8000)
    client.chat_client()