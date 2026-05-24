# writer:enjoyiii
# 2026年05月21日23时12分59秒
# 15211281589@163.com
from multiprocessing import Pool
import os,time,random

def work(i):
    start=time.time()
    # 耗时操作
    print(f'进程{os.getpid()}正在执行任务{i}')
    time.sleep(random.randint(1,3))
    print(f'进程{os.getpid()}正在执行任务{i}，耗时{time.time() - start}s')


if __name__ == '__main__':
    po=Pool(3)#进程池3个进程
    for i in range(10):
        po.apply_async(work,args=(i,))#异步派任务
    print('父进程已经派活完毕')
    time.sleep(1)
    po.terminate()#杀死进程池
    # po.close()#关闭进程池
    po.join()#等待进程池结束