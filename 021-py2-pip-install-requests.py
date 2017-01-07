#-*- coding: utf-8 -*-
#coding=utf-8
# __author__ = 'zy'

#-*- coding: utf-8 -*-
#coding=utf-8
# __author__ = 'zy'
# Python爬虫利器一之Requests库的用法
# http://cuiqingcai.com/2556.html
import requests
#r = requests.get("http://baidu.com")
inlinepa = {"a":"a"};
r = requests.get("http://baidu.com",params=inlinepa)
print type(r)
print r.status_code
print r.encoding
print r.text
print r.cookies
