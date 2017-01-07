#-*- coding: utf-8 -*-  
#coding=utf-8

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    print 'args=',args
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()



try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO


try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5