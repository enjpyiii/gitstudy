# writer:enjoyiii
# 2026年05月21日16时26分25秒
# 15211281589@163.com
from multiprocessing import Process
import time

def run_proc(name,age,**kwargs):
    print('my name is %s,my age is %s'%(name,age))
    print(kwargs)
    exit(5)

if __name__ == '__main__':
    p = Process(target=run_proc,args=('enjoyiii',18),kwargs={'sex':'male','city':'changsha'})
    p.start()
    # time.sleep(5)#等待子进程创建
    print(p.is_alive())
    p.join()#等待子进程结束
    # time.sleep(5)#等待父进程结束
    print(f'子进程退出码：{p.exitcode}')
    print('父进程结束')
