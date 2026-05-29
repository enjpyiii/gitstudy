# writer:enjoyiii
# 2026年05月25日18时41分18秒
# @163.com
def fib(n):
    num1, num2 = 0, 1
    current=0
    while current<n:
        num=num1
        num1, num2 = num2, num1+num2
        current+=1
        yield num#整个cpu变量被冻结,执行next之后会从被冻结的地方继续往上循环
    return 'done'

if __name__ == '__main__':
    f=fib(10)
    for i in f:
        print(i)