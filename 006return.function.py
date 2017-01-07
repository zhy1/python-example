#-*- coding: utf-8 -*-  
#coding=utf-8

#return function

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print calc_sum(1,2,3,4);


#循环调用
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#输出函数结果发现是一个函数
print lazy_sum(1,2,3);

#运行输出的函数
func = lazy_sum(1,2,3);
print func();

#直接2重运行
print lazy_sum(1,2,3)();

runnerA =  lazy_sum(1,2,3);
runnerB =  lazy_sum(1,2,3);
#每次生成一次
print runnerA==runnerB


#闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1()
print f2()
print f3()






#闭包循环变量值域变化控制

def count():
     fs = []
     for i in range(1, 4):
         def f(j):
             def g():
                 return j*j
             return g
         fs.append(f(i))
     return fs



f1, f2, f3 = count()
print f1()
print f2()
print f3()


#匿名函数

print  map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#   通过对比可以看出，匿名函数lambda x: x * x实际上就是：
#
#   def f(x):
#       return x * x
#   关键字lambda表示匿名函数，冒号前面的x表示函数参数。


# 匿名函数赋值给变量
print '匿名函数赋值给变量'
f = lambda x: x * x
print f
print f(5)


# 匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y



#  装饰器
def nowe():
     print '2013-12-25'

# 对象＝函数
e = nowe
# 运行函数
e()

