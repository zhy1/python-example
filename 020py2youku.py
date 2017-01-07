#-*- coding: utf-8 -*-
#coding=utf-8
# __author__ = 'zy'

import urllib,urllib2,sys,os
from BeautifulSoup import BeautifulSoup
import itertools,re
# 用Python实现Youku视频批量下载　版本：Python2.7+BeautifulSoup3.2.1
url_i =1
pic_num = 1

#自己定义的引号格式转换函数
def _en_to_cn(str):
    obj = itertools.cycle(['“','”'])
    _obj = lambda x: obj.next()
    return re.sub(r"['\"]",_obj,str)

if __name__ == '__main__':
    #下载连续3个网页的视频
    while url_i <= 3:
        webContent = urllib2.urlopen("http://news.youku.com/focus/index/_page26716_" + str(url_i) + ".html")
        data = webContent.read()
        #利用BeautifulSoup读取视频列表网页数据
        soup = BeautifulSoup(data)
        print "-------------------------Page " + str(url_i) + "-------------------------"
        #获得相应页面的视频thumbnail和title的list
        tag_list_thumb = soup.findAll('li','v_thumb')
        tag_list = soup.findAll('li', "v_title")
        for item in tag_list:
            #通过每个thumbnail中的herf导向视频播放页面
            web_video_play = urllib2.urlopen(item.a['href'])
            data_vp = web_video_play.read()
            #利用BeautifulSoup读取视频播放网页数据
            soup_vp = BeautifulSoup(data_vp)
            #找到“下载”对应的链接
            tag_vp_list = soup_vp.findAll('a', id = 'fn_download')
            for item_vp in tag_vp_list:
                #将下载链接保存到url_dw中
                url_dw = '"' + item_vp['_href'] + '"'
                print item.a['title'] + ": " + url_dw
                #调用命令行运行iku下载视频，需将iku加入环境变量
                os.system("iku " + url_dw)
        #保存每个视频的thumbnail
        for item_thumb in tag_list_thumb:
            urllib.urlretrieve(item_thumb.img['src'], "E:\\下载视频\\thumbnails\\" + str(pic_num) + "." +
                               _en_to_cn(item_thumb.img['title']) + ".jpg")
            pic_num += 1
        print "--------------------------------------------------------------"
        print "--------Page " + str(url_i) + "'s video thumbnails have  been saved!"
        url_i += 1