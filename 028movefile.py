# -*- coding: utf-8 -*-
# coding=utf-8
# __author__ = 'zy'


import os
import shutil
import time
import datetime

s = os.sep  # 根据unix或win，s为\或/
# root = "d:" + s + "ll" + s #要遍历的目录
origin = "/Users/zy/Downloads/a/"  # 不会被改变
root = "/Users/zy/Downloads/a/"  # 会被改变


def changeMoveFile(dirs, f):  # 回调函数的定义
    fileNameAsDate = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    fname = os.path.splitext(f)  # 分割 文件名 和 扩展名 数组

    suffix = ".mp4"
    new = fname[0] + suffix  # 改文件名字
    idx = new.index('.')!=0
    # 隐藏文件不理会
    if idx:
    # 如果 有上级目录则加上 以准确获得当前路径
        if len(dirs):
            current = origin + dirs[0] + s
        else:
            current = origin + s

        remoteUrl = origin + fname[0] + "-"+ fileNameAsDate + suffix
        localUrl = current + f


        # print(current+fname[0])
        # print(current +new+fileNameAsDate)

        if os.path.exists(origin + new):
            if os.path.exists(remoteUrl):
                changeMoveFile(dirs, f)
            else:
                print("start move:\n" + localUrl + " ---to:---\n" + remoteUrl + "\n")
                fileNameAsDate = time.strftime('%Y%m%d-%H%M%S.%f', time.localtime(time.time()))
                # shutil.move(localUrl, remoteUrl)
                os.rename(localUrl, remoteUrl)
                # print(current+new+" exists!, \nuse:\n"+ current + fname[0] + fileNameAsDate + suffix);

        else:
            print("start move:\n" + localUrl + " ---to---\n" + remoteUrl + "\n")
            # shutil.move(localUrl, current + new)
            os.rename(localUrl, origin + new)


# 严重逻辑错误,又传入了文件夹  又传入文件 todo
for root, dirs, files in os.walk(root):
    for f in files:
        if os.path.splitext(f)[0]:
            changeMoveFile(dirs,f)



