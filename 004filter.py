#-*- coding: utf-8 -*-  
#coding=utf-8



#filter()函数用于过滤序列。
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


#一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 结果: ['A', 'B', 'C']