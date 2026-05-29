# writer:enjoyiii
# 2026年05月25日21时26分47秒
# @163.com
from greenlet import greenlet
import time
def test1():
    while True:
        print("---1---")
        time.sleep(0.5)
        gr2.switch()
def test2():
    while True:
        print("---2---")
        time.sleep(0.5)
        gr1.switch()

if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()