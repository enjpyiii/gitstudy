# writer:enjoyiii
# 2026年05月25日15时56分16秒
# @163.com
class FibIter:# 斐波那契数列
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.n1 = 0
        self.n2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            num=self.n1
            self.n1, self.n2 = self.n2, self.n1 + self.n2
            self.current += 1
            return num
        else:
            raise StopIteration

if __name__ == '__main__':
    fib = FibIter(10)
    for i in fib:
        print(i,end=' ')
    print()
    li=list(FibIter(15))
    print(li)
    tp=tuple(FibIter(8))
    print(tp)