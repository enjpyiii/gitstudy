# writer:enjoyiii
# 2025年05月26日21时31分20秒
# 1663472473@qq.com
import operator
from operator import itemgetter
a=[5,6,1,18,3]
# a.sort()
# print(a)#sort只改变列表本身，sorted会返回一个新的列表，sort和sorted都是稳定的
print(sorted(a))
dict1={'1':'enjoy','3':'iii','2':'joy','5':'ddd','4':'dodo'}
print(sorted(dict1))#只给字典中的键排序，不给值排序
str_list='This is a test string from Andrew'.split()
print(sorted(str_list))#排出来是字典序
print(sorted(str_list,key=str.lower))
#alt+shift 竖选
#列表嵌元组排序
student_tuples=[('enjoy','D',15),
                ('jane','B',16),
                ('dave','C',17)]
print(sorted(student_tuples,key=lambda x:x[1]))
print(sorted(student_tuples,key=itemgetter(0)))
print('多级排序')
print(sorted(student_tuples,key=itemgetter(0,1)))#先按照名字排序，名字相同时按照等级排序

#lambda匿名函数：只用一次，阅读效率高lambda 入参：返回值
#itemgetter主要用于python自带数据类型如列表元组等，attrgetter用于自定义对象排序
class student:
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age
    def __repr__(self):
        return repr((self.name,self.grade,self.age))
#类的排序
student_objects=[
    student('enjoyiii','A',15),
    student('amanda','C',12),
    student('David','B',10)
]
print(sorted(student_objects,key=lambda student:student.age))
print(sorted(student_objects,key=operator.attrgetter("grade")))
print('多级排序')
print(sorted(student_objects,key=operator.attrgetter("grade","age")))#先按照grade排序，grade相同时按照age排序
#字典嵌列表排序
print('-'*50)
my_dict={'enjoyiii':[18,'female'],'joyiii':[15,'male'],'wangdao':[10,'unknown']}
print(sorted(my_dict.items(),key=lambda x:x[1][0]))#items（）返回的是字典的键值对，结果是用列表嵌元组表示，x【0】是键，x【1】是值
print('-'*50)
# 列表嵌字典排序
print('-'*50)
gameresult=[{'name':'joyiii','win':10,'lose':3,'rating':75},
            {'name':'enjoyiii','win':3,'lose':5,'rating':57},
            {'name':'Bob','win':4,'lose':5,'rating':57},
            {'name':'Patty','win':9,'lose':3,'rating':71.48}]
print(sorted(gameresult,key=itemgetter('rating','win')))
print(sorted(gameresult,key=lambda x:(x['rating'],-x['win'])))#rating元素升序，win元素降序
print('-'*50)
listx=[(3,5),(1,2),(2,4),(3,1),(1,3)]
print(sorted(listx,key=lambda x:(x[0],-x[1])))#第一个元素升序，在第一个元素相等时按照第二个元素降序排列