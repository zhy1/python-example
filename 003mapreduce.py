#-*- coding: utf-8 -*-  
#coding=utf-8
#列表生成器
print [x*x for x in range(1,10)]

#高阶函数
print abs(-10);


#map reduce

#map
def ff(x):
     return x * x
print map(ff, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#计算list返回list


#reduce 
def add(x, y):
     return x + y
print reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#=1+2)+3)+4)+5)+6)+7)+8)+9)把前面的结果返回给后面的参数