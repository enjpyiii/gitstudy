# writer:enjoyiii
# 2026年05月24日19时55分27秒
# 15211281589@163.com
import threading
import time
g_num=0
def work1(num):
    global g_num
    for i in range(num):
        g_num+=1
    print('in work1 g_num=%d' % g_num)

def work2(num):
    global g_num
    for i in range(num):
        g_num+=1
    print('in work2 g_num=%d' % g_num)

count=10000000
t1=threading.Thread(target=work1,args=(count,))
t1.start()
t2=threading.Thread(target=work2,args=(count,))
t2.start()
t1.join()
t2.join()
print('main thread g_num=%d' % g_num)#在python3.12上面执行还能得到正确结果，但是在linux上执行就没法得到正确结果了，所以需要加锁