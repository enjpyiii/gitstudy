# writer:enjoyiii
# 2026年05月21日17时04分34秒
# 15211281589@163.com
from multiprocessing import Process
import time
# windows上面编译不通，子进程会影响父进程对于文件的读取
def read_file():
    time.sleep(2)
    my_file = open('test.txt', 'rb')
    #读取文件内容
    content=my_file.read(5)
    print(f'子进程读取的内容：{content.decode("utf-8")}')#子进程读到的是写之后的内容
    my_file.close()

if __name__ == '__main__':
    #创建子进程
    p=Process(target=read_file)
    p.start()
    # time.sleep(5)
    # 打开文件
    file = open('test.txt', 'rb+')
    file.write(b'howareyou')
    file.close()
    #等待子进程结束
    p.join()