# writer:enjoyiii
# 2026年05月21日16时44分17秒
# 15211281589@163.com
import os
from multiprocessing import Process
import time
nums=[11,22]

def work1():
    print('in precess1 pid=%d,nums=%s' % (os.getpid(), nums))
    for i in range(5):
        nums.append(i)
        time.sleep(1)
        print('in precess1 pid=%d,nums=%s' % (os.getpid(), nums))



if __name__ == '__main__':
    p1=Process(target=work1)
    p1.start()
    p1.join()

    print('in main precess pid=%d,nums=%s' % (os.getpid(), nums))