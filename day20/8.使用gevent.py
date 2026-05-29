# writer:enjoyiii
# 2026年05月25日21时36分48秒
# @163.com
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)#不能使用time.sleep()，因为gevent.sleep()是切换协程的，time.sleep()是阻塞线程

gr1=gevent.spawn(f,5)
gr2=gevent.spawn(f,5)
gr3=gevent.spawn(f,5)
gr1.join()
gr2.join()
gr3.join()