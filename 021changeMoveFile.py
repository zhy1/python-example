#-*- coding: utf-8 -*-
#coding=utf-8
# __author__ = 'zy'


import os
import shutil
import time
# import strftime from time
import datetime
# import time
# print time.mktime(datetime.datetime.now().timetuple())

s = os.sep #根据unix或win，s为\或/
# root = "d:" + s + "ll" + s #要遍历的目录
root = "/Users/zy/Downloads/a/"

		# fileNameAsDate = strftime(time.time())
# fileNameAsDate = time.strftime('%Y%m%d',time.localtime(time.time()))
# fileNameAsDate = time.strftime("%Y%m%d-%H%M%p-%f", time.localtime())
# fileNameAsDate = time.strftime("%Y%m%d-%H%M%S-%f", time.localtime())
#_______________________v3_________________________________________

def changeMoveFile(dire,f): #回调函数的定义
        fname = os.path.splitext(f)  # 分割 文件名 和 扩展名 数组
        # new = fname[0] + 'x' + fname[1]  # 改文件名字: 文件名＋ x + 扩展名
        # if(fname[0].index('-')
        new = fname[0]+ ".mp4"  # 改文件名字
		fileNameAsDate = time.strftime("%Y%m%d-%H%M%S-%f", time.localtime())
        print(dire+f)
        print(root+new+fileNameAsDate)
        # if os.path.exists(root + new):
        	# repeatNumber = repeatNumber? ++repeatNumber: 0;
        	# changeMoveFile(dire,f,repeatNumber)
        	# print(root+new+"exists!, use file name + datatime = new  file name.");
        # else:
			# fileNameAsDate = time.strftime('%Y%m%d-%H%M%S-%f',time.localtime(time.time()))
        	# os.rename(os.path.join(dire,f),os.path.join(root,new)) #重命名
			# shutil.move(dire+f,root+fileNameAsDate+new)    

#________________________________________________________________

#_______________________v2_________________________________________

def changeFileName(dire,f): #回调函数的定义
        fname = os.path.splitext(f)  # 分割 文件名 和 扩展名 数组
        # new = fname[0] + 'x' + fname[1]  # 改文件名字: 文件名＋ x + 扩展名
        new = fname[0]+ ".mp4"  # 改文件名字
        os.rename(os.path.join(dire,f),   os.path.join(dire,new)) #重命名

#________________________________________________________________

#_______________________v1_________________________________________
def changeDirFileName(args,dire,fis): #回调函数的定义
    for f in fis:
        fname = os.path.splitext(f)  # 分割 文件名 和 扩展名 数组
        # new = fname[0] + 'x' + fname[1]  # 改文件名字: 文件名＋ x + 扩展名
        new = fname[0]+ ".mp4"  # 改文件名字
        os.rename(os.path.join(dire,f),   os.path.join(dire,new)) #重命名

# os.path.walk(root,changeDirFileName,()) #遍历 不递归
#________________________________________________________________



for root, dirs, files in os.walk(root):
	for f in files:
		changeMoveFile(root,f)