#coding:utf-8import osimport sys;# reload(sys);# sys.setdefaultencoding("utf8")# import sys# sys.setdefaultencoding('utf-8')path = '/Users/zy/Downloads/pdf/'generatorWalk= os.walk(path)fileLists = []for root, dirs, files in os.walk(path):    # files  是一个内存地址  直接输入不会受到任何转码指令的影响    print("Root=",root, "dirs = ", dirs, "files = ", str(files))    # decode('gbk').encode('utf-8'))#	a = eval("u"+root)#	b = eval("u"+dirs)#	c = eval("u"+files)## root.decode('gb2312').encode('utf-8')