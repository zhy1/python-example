#-*- coding: utf-8 -*-  
#coding=utf-8

#  装饰器
def nowe():
     print '2014-07-08'

# 对象＝函数
e = nowe
# 运行函数
e()

#_________________装饰器是指在函数定义时，
#   使用类似java注解的形式写在函数前面
#   可以在调用函数时被动先调用装饰器
#   类似于@before


# 定义一个装饰器

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        print '装饰器在20160118以前运行了但是我门没有调用装饰器'
        return func(*args, **kw)
    return wrapper


# 放到函数前面的装饰器

@log
def nowb():
    print '2016-01-18'


# 调用被装饰过的函数
nowb();





# Python的functools模块提供了很多有用的功能，
# 其中一个就是偏函数（Partial function）。
# 要注意，这里的偏函数和数学意义上的偏函数不一样。


# 字符串转化
print int('12345');

# 字符串转化8进制
print int('12345',base=8);

# 字符串转化16进制
print int('12345',16);

# 字符串转化2进制 并使用functools中的二进制转换器partial
import functools
int2 = functools.partial(int,base=2)
print int2('10000000000')