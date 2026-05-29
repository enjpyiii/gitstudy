# writer:enjoyiii
# 2026年05月25日21时57分20秒
# @163.com
from gevent import monkey
monkey.patch_all()
import requests#默认自带的爬虫库
import gevent,time

def my_download(url):
    print('开始下载%s'%url)
    try:
        response=requests.get(url,timeout=5)
        data=response.text
        print('%d bytes received from %s.'%(len(data),url))
    except Exception as e:
        print('Error:',e)

if __name__=='__main__':
    start=time.time()
    gevent.joinall([
        gevent.spawn(my_download,'https://www.baidu.com'),
        gevent.spawn(my_download,'https://www.taobao.com'),
        gevent.spawn(my_download,'https://www.jd.com'),
    ])
    end=time.time()
    print('Total time: %.5f seconds'%(end-start))

