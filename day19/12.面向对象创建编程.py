# writer:enjoyiii
# 2026年05月24日19时28分56秒
# 15211281589@163.com
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg="I'am"+self.name+'@'+str(i)#name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t=MyThread()
    t.start()
    t.join()#等待线程结束