import urllib
import urllib2
# import requests.packages.urllib3.util.ssl_


# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
#url="http://www.udfex.com/05-udf-ecw/pub/price/calc.json?levelCode=VIP3&serviceProductCode=USS&unit=kg&v=1453108258575&weight=2"
url = 'http://mm.taobao.com/json/request_top_list.htm?page=1'


request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()