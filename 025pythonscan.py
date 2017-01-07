#coding:utf-8

import os
path = '/Users/zy/Downloads/pdf/'
for root, dirs, files in os.walk(path):
	for f in files:
		print str(f)


# 直接输出无法转码。 是输出内存的值
# print("Root=",root, "dirs = ", dirs, "files = ", str(files))

