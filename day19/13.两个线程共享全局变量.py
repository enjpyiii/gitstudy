# writer:enjoyiii
# 2026年05月24日19时38分49秒
# 15211281589@163.com
from threading import Thread
import time

g_num=100

def work1():
    global g_num
    for i in range(3):
        g_num+=1

    print('in work1 g_num=%d' % g_num)

def work2():
    global g_num
    time.sleep(0.1)
    print('in work2 g_num=%d' % g_num)

if __name__ == '__main__':
    print('线程创建之前 g_num=%d' % g_num)

    t1=Thread(target=work1)
    t1.start()
    # #延时一会，保障线程1结束
    # time.sleep(1)
    t2=Thread(target=work2)
    t2.start()

    t1.join()
    t2.join()