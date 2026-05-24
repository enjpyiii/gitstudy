# writer:enjoyiii
# 2026年05月22日09时27分07秒
# 15211281589@163.com
import time
from threading import Thread

def say_hello():
    print('hello world')
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = Thread(target=say_hello)
        t.start()