#-*- coding: utf-8 -*-  
#coding=utf-8




import urllib2

#urlopen(url, data, timeout)

response = urllib2.urlopen("http://www.baidu.com")
#print response.read()



#step2

import urllib2
 
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
#print response.read()



import urllib
import urllib2
 
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
#print response.read()


urls="http://www.udfex.com/05-udf-ecw/pub/price/calc.json?levelCode=VIP3&serviceProductCode=USS&unit=kg&v=1453108258575&weight=2"

request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()