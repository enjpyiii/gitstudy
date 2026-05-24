# writer:enjoyiii
# 2026年05月21日20时02分12秒
# 15211281589@163.com
from multiprocessing import Process,Queue
import time

def write(q):
    print('写数据进程开始')
    for i in range(10):
        print(f'写入{i}')
        q.put(i)
        time.sleep(0.42018299)

def read(q):
    while True:
        if not q.empty():
            data=q.get()
            print(f'读到数据{data}')
            time.sleep(0.5)
        else:
             break

if __name__ == '__main__':
    q=Queue()
    p1=Process(target=write,args=(q,))
    p2=Process(target=read,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()