# writer:enjoyiii
# 2026年05月25日18时51分34秒
# @163.com
def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1

if __name__=='__main__':
    g=gen()
    print(next(g))
    print(g.send('hello'))