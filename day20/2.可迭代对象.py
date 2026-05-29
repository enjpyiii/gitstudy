# writer:enjoyiii
# 2026年05月25日15时16分03秒
# @163.com
from collections.abc import Iterable

class MyIterator(object):
    def __init__(self, mylist):
        self.mylist = mylist
        self.index = 0
    def __next__(self):
        if self.index < len(self.mylist.container):
            item = self.mylist.container[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
    def __iter__(self):
        return self# 返回迭代器对象,迭代器必须写

class MyList(object):
    def __init__(self):
        self.container=[]
    def add(self, item):
        self.container.append(item)
    def __iter__(self):
        """
        \要实现可迭代对象，需要实现__iter__方法，该方法返回一个迭代器对象
        :return:
        """
        return MyIterator(self)

my_list = MyList()
my_list.add(1)
my_list.add(2)
my_list.add(3)

print(isinstance(my_list, Iterable))