# writer:enjoyiii
# 2026年05月24日19时38分49秒
# 15211281589@163.com
from threading import Thread
import time,threading


def work1(my_list,lock):
    lock.acquire()
    for i in range(3):
        my_list.append(i)
    print(f'in work1 my_list={my_list}')
    lock.release()

def work2(my_list, lock):
    lock.acquire()
    for i in range(3,6):
        my_list.append(i)
    print(f'in work2 my_list={my_list}')
    lock.release()

def main():
    my_list= []
    lock= threading.Lock()#初始化锁
    t1=Thread(target=work1,args=(my_list,lock))
    t1.start()
    # #延时一会，保障线程1结束
    # time.sleep(1)
    t2=Thread(target=work2,args=(my_list,lock))
    t2.start()

    t1.join()
    t2.join()
    print(f'in main my_list={my_list}')

if __name__ == '__main__':
    main()

