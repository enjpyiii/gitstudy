# writer:enjoyiii
# 2026年05月22日09时35分13秒
# 15211281589@163.com
from threading import Thread
import threading
import time

def sing():
    for i in range(3):
        print('%d正在唱歌：%s'%(i,time.ctime()))
        time.sleep(1)
def dance():
    for i in range(3):
        print('%d正在跳舞：%s'%(i,time.ctime()))
        time.sleep(1)

if __name__ == '__main__':
    print('----开始----：%s'%time.ctime())
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
    #线程数目
    print('线程数目：%d'%threading.active_count())
    t1.join()
    t2.join()