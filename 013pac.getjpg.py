#-*- coding: utf-8 -*-  
#coding=utf-8



import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# html = getHtml("http://tieba.baidu.com/p/2738151262")
html = getHtml("http://tieba.baidu.com/f?kw=www&fr=wwwt")

print html