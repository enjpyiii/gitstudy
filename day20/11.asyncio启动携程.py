# writer:enjoyiii
# 2026年05月25日22时35分43秒
# @163.com
import asyncio

async def fetch_data(delay,name):
    print('开始下载%s,delay=%d'%(name, delay))
    await asyncio.sleep(delay)
    print('%s下载完成'%name)
    return '数据%s'%name

async def main():
    tasks=[
        fetch_data(3,'task1'),
        fetch_data(2,'task2'),
        fetch_data(1,'task3'),
    ]

    #并发执行所有任务，等待他们完成，gather（*tasks）返回一个列表
    results=await asyncio.gather(*tasks)

if __name__=='__main__':
    asyncio.run(main())