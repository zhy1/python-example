# -*- coding: utf-8 -*-
# coding=utf-8
# __author__ = 'zy'


import os
import shutil
import time
import datetime

s = os.sep  # 根据unix或win，s为\或/
# root = "d:" + s + "ll" + s #要遍历的目录
# origin = "/Users/zy/Downloads/a/"  # 不会被改变

# 所有问题都会被移动到root目录,入参和移动目标的考量
root = "/Users/zy/Downloads/a/"

# 所有被移动文件的后缀名
suffix = ".mp4"

# current (current directory + system support route separator)  当前的操作目录+当前系统支持的路径分割符号
# origin  (current directory)   当前的操作目录
# remoteUrl  (target time name) 如果移动之后的文件名已经存在,一个带着年月日时分秒的新名字
# localUrl   (file current name)    文件的当前地址

def changeMoveFile(origin,dirs,f):  # 回调函数的定义
    fileNameAsDate = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    fname = os.path.splitext(f)  # 分割 文件名 和 扩展名 数组

    new = fname[0] + suffix  # 改文件名字
    idx = new.index('.')!=0
    # 隐藏文件不理会
    if idx:
        # 如果 有上级目录则加上 以准确获得当前路径
        current = origin + s

        remoteUrl = root + fname[0] + "-"+ fileNameAsDate + suffix
        localUrl = current + f


        # print(current+fname[0])
        # print(current +new+fileNameAsDate)
        # 当前url+新名字 != 当前url+ 老名字
        if new != f or root!= origin:
            if os.path.exists(root + new):
                if os.path.exists(remoteUrl):
                    time.sleep(0.1)
                    changeMoveFile(origin,dirs,f)
                else:
                    print("start rename move:\n" + localUrl + " ---to:---\n" + remoteUrl + "\n")
                    fileNameAsDate = time.strftime('%Y%m%d-%H%M%S.%f', time.localtime(time.time()))
                    # shutil.move(localUrl, remoteUrl)
                    os.rename(localUrl, remoteUrl)
                    # print(current+new+" exists!, \nuse:\n"+ current + fname[0] + fileNameAsDate + suffix);
            else:
                print("start move:\n" + localUrl + " ---to---\n" + root + new + "\n")
                os.rename(localUrl, root + new)


# 严重逻辑错误,又传入了文件夹  又传入文件 todo
# for root, dirs, files in os.walk(root):
#     for f in files:
#         if os.path.splitext(f)[0]:
#             changeMoveFile(f)

# http://blog.csdn.net/thy38/article/details/4496810
#  http://www.cnblogs.com/dreamer-fish/p/3820625.html
# orgin , dirs , files 是 walk这个查询行为的一次查询结果 而不是返回对象
for origin, dirs, files in os.walk(root):
    for f in files:
        if os.path.splitext(f)[0]:
            changeMoveFile(origin,dirs,f)


