#-*- coding: utf-8 -*-  
#coding=utf-8

#import re
import urllib2
#import urllib.request
#import json
#import time
#import random
#import sys

url="http://www.baidu.com"
response = urllib2.urlopen(url)
print response.read()
print response.getUrl()
response.close()