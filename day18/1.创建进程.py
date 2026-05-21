# writer:enjoyiii
# 2026年05月21日14时06分06秒
# 15211281589@163.com
from multiprocessing import Process

import time
def run_proc():
    while True:
        print('---2---')
        time.sleep(1)

if __name__ == '__main__':
    # run_proc()#此时只会打印2
    p=Process(target=run_proc)#只写函数名不写括号，回调函数
    p.start()
    while True:
        print('---1---')
        time.sleep(1)