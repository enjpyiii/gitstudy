# writer:enjoyiii
# 2026年05月25日21时48分06秒
# @163.com
import gevent
from gevent import monkey
import time,random,gevent
monkey.patch_all()

def coroutine_work(coroutine_name):
    for i in range(5):
        print(coroutine_name,i)
        time.sleep(random.random())#表示睡0-1之间的一个小数

gevent.joinall( [
    gevent.spawn(coroutine_work,'coroutine_1'),
    gevent.spawn(coroutine_work,'coroutine_2'),
])