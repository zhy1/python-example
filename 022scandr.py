#-*- coding: utf-8 -*-
#coding=utf-8
# __author__ = 'zy'


import os
import sys;
# reload(sys);
# sys.setdefaultencoding("utf8")

# import sys
# sys.setdefaultencoding('utf-8')

path = '/Users/zy/Downloads/'

generatorWalk= os.walk(path)
fileLists = []




# for root, dirs, files in os.walk(path):
for root,dirs,files in generatorWalk:
    atom = {"dirs": root, "dirs": dirs,"files":files }
    fileLists.append(atom)
    # print("Root=",root, "dirs = ", dirs, "files = ", files)
print (fileLists)


#	a = eval("u"+root)
#	b = eval("u"+dirs)
#	c = eval("u"+files)

## root.decode('gb2312').encode('utf-8')
