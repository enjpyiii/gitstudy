# writer:enjoyiii
# 2026年05月21日16时03分12秒
# 15211281589@163.com
from multiprocessing import Process
import os
import time

def run_proc():
    print('子进程%s启动，父进程%s' % (os.getpid(), os.getppid()))
    print('子进程将要结束')

if __name__ == '__main__':
    print('父进程%s启动' % os.getpid())
    p = Process(target=run_proc)
    p.start()
    time.sleep(20)#父进程在睡觉，子进程运行完后没人管那么久会变成僵尸进程