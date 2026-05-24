# writer:enjoyiii
# 2026年05月21日17时04分34秒
# 15211281589@163.com
from multiprocessing import Process
import time
def modify_list(my_list):
    my_list.append(4)
    print(my_list)

if __name__ == '__main__':
    #打开文件
    file = open('test.txt', 'r')
    #创建子进程
    my_list=[1,2,3]
    p=Process(target=modify_list,args=(my_list,))
    p.start()
    # time.sleep(5)
    #等待子进程结束
    p.join()
    print(f'主进程中的mylist：{my_list}')