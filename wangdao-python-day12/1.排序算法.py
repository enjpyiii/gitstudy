# writer:enjoyiii
# 2025年05月22日18时44分48秒
# 1663472473@qq.com
import random
import sys
import time

sys.setrecursionlimit(2000)


class Sort:
    def __init__(self, arr_range, num_range):
        self.arr = []
        self.arr_range = arr_range
        self.num_range = num_range
        self.creat_random_num()
        self.arr_b=[0]*arr_range#为了归并排序使用的队列

    def creat_random_num(self):
        for i in range(self.arr_range):
            self.arr.append(random.randint(0, self.num_range-1))#randint是左闭右闭的

    # def bubble_sort(self):#冒泡排序
    #     for j in range(self.arr_range - 1):
    #         for i in range(self.arr_range - 1):
    #             if self.arr[i] > self.arr[i + 1]:
    #                 temp = self.arr[i]
    #                 self.arr[i] = self.arr[i + 1]
    #                 self.arr[i + 1] = temp
    #     print(self.arr)
    def bubble_sort(self):
        for i in range(self.arr_range,1,-1):
            non_change=True
            for j in range(i-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
                    non_change=False
            if non_change:
                break

    def select_sort(self):
        for i in range(self.arr_range - 1):
            min_post = i
            for j in range(i + 1, self.arr_range):
                if self.arr[min_post] > self.arr[j]:
                    min_post = j
            self.arr[min_post], self.arr[i] = self.arr[i], self.arr[min_post]
        print(self.arr)

    def insert_sort(self):
        for i in range(1, self.arr_range):
            cur_num = self.arr[i]
            for j in range(i - 1, -1, -1):
                if cur_num < self.arr[j]:
                    self.arr[j + 1] = self.arr[j]
                    self.arr[j] = cur_num
                else:
                    break
        print(self.arr)
        # for i in range(1,self.arr_range):#老师的写法
        #     insert_val=self.arr[i]
        #     j=i-1
        #     while j>=0:
        #         if self.arr[j]>insert_val:
        #             self.arr[j+1]=self.arr[j]
        #         else:
        #             break
        #         j-=1
        #     self.arr[j+1]=insert_val

    def shell_sort(self):
        arr = self.arr
        gap = self.arr_range >> 1
        # 将五个一改成五个gap
        while gap > 0:
            for i in range(gap,self.arr_range):
                insert_value = arr[i]
                j = i - gap
                while j >= 0:
                    if arr[j] > insert_value:
                        arr[j + gap] = arr[j]
                    else:
                        break
                    j -= gap
                arr[j + gap] = insert_value
            gap = gap >> 1
        print(arr)

    def partition(self, left, right):
        arr = self.arr
        k = left
        # 随机选取分隔值然后和right位置进行交换
        random_pos=random.randint(left, right)
        self.arr[right], self.arr[random_pos] = self.arr[random_pos], self.arr[right]
        for i in range(left, right):#把最右边作为分割值
            if self.arr[i] < self.arr[right]:
                self.arr[i], self.arr[k] = self.arr[k], self.arr[i]
                k += 1
        self.arr[k], self.arr[right] = self.arr[right], self.arr[k]
        return k

    def quick_sort(self, left, right):#快排时间复杂度O(nlog2n),最快情况：O(n**2);空间复杂度O(logn)
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def adjust_dad_pos(self, dad_pos, cur_arrlen):
        dad = dad_pos
        son = dad * 2 + 1
        while son<cur_arrlen:
            if son+1<cur_arrlen and self.arr[son+1]>self.arr[son]:
                son+=1
            if self.arr[son]>self.arr[dad]:
                self.arr[son],self.arr[dad]=self.arr[dad],self.arr[son]
                dad=son
                son=dad*2+1
            else:
                break
    def heap_sort(self):
        for i in range((self.arr_range-1)//2,-1,-1):
            self.adjust_dad_pos(i,self.arr_range)
        for i in range(self.arr_range-1,0,-1):
            self.arr[0],self.arr[i]=self.arr[i],self.arr[0]
            self.adjust_dad_pos(0,i)
    def merge(self,low,mid,high):
        arr_b=self.arr_b
        arr=self.arr
        for i in range(self.arr_range):
            arr_b[i]=arr[i]
        i=low
        j=mid+1
        k=low
        while i<=mid and j<=high:
            if arr_b[i]<arr_b[j]:
                arr[k]=arr_b[i]
                k+=1
                i+=1
            else:
                arr[k]=arr_b[j]
                k+=1
                j+=1
        while i<=mid:
            arr[k] = arr_b[i]
            k += 1
            i += 1
        while j<=high:
            arr[k] = arr_b[j]
            k += 1
            j += 1

    def merge_sort(self,low,high):
        if low<high:
            mid=(low+high)//2
            self.merge_sort(low,mid)
            self.merge_sort(mid+1,high)
            self.merge(low,mid,high)
    def cal_sort_time(self,sort_method,*args,**kwargs):
        start=time.time()
        sort_method(*args,**kwargs)
        end=time.time()
        print(f'消耗的时间：{end-start}')

    def count_sort(self):
        arr=self.arr
        count_arr=[0]*self.num_range#统计每个数出现的次数
        for i in arr:
            count_arr[i]+=1
        # k=0
        # for i in range(self.num_range):
        #     for j in range(count_arr[i]):
        #         arr[k]=i
        #         k+=1

if __name__ == '__main__':
    sort = Sort(100000, 1000)
    print(sort.arr)
    # sort.bubble_sort()
    # sort.select_sort()
    # sort.insert_sort()
    # sort.shell_sort()
    # sort.quick_sort(0, sort.arr_range-1)
    # sort.heap_sort()
    # sort.merge_sort(0,9)
    # sort.count_sort()
    sort.cal_sort_time(sort.count_sort)
    # print(sort.arr)