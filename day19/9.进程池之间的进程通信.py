# writer:enjoyiii
# 2026年05月22日00时00分39秒
# 15211281589@163.com
from multiprocessing import Manager,Pool
import time,random,os

def reader(q):
    print('reader 启动(%s),父进程为(%s)'%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print('reader 从队列中获取数据%s'%q.get(True))

def writer(q):
    print('writer 启动(%s),父进程为(%s)' % (os.getpid(), os.getppid()))
    for i in 'wangdao':
        q.put(i)

if __name__ == '__main__':
    #显示当前进程pid
    print('当前进程pid为(%s)'%os.getpid())
    q = Manager().Queue()
    po = Pool(3)
    po.apply_async(writer,args=(q,))
    time.sleep(1)
    po.apply_async(reader,args=(q,))
    po.close()
    po.join()
    print('父进程(%s)结束'%os.getpid())