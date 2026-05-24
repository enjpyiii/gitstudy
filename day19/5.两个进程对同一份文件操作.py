# writer:enjoyiii
# 2026年05月21日17时04分34秒
# 15211281589@163.com
from multiprocessing import Process
import time
# windows上面编译不通，子进程会影响父进程对于文件的读取
def read_file(my_file):
    #读取文件内容
    content=my_file.read(5)
    print(f'子进程读取的内容：{content}')

if __name__ == '__main__':
    #打开文件
    file = open('test.txt', 'r', encoding='utf-8')
    #创建子进程
    p=Process(target=read_file,args=(file,))
    p.start()
    # time.sleep(5)
    #等待子进程结束
    p.join()
    maincontent=file.read(5)
    print(f'主进程中的maincontent：{maincontent}')
    file.close()