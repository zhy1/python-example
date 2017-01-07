#coding=utf-8
# __author__ = 'zy'
import os
import time


# import sys
# import importlib
# importlib.reload(sys)

# sys.setdefaultencoding('utf-8')

# path = '/Users/zy/Downloads/pdf'
# path = unicode(path , "utf-8")


# path = '/Library/WebServer/Documents'
# path = '/Users/zy/Downloads/pdf'
path = '/Users/zy/Documents'

def getAllFiles():
	generatorWalk= os.walk(path)
	fileLists = []
	for root,dirs,files in generatorWalk:
		atom = {"files":files }
		fileLists.append(atom)
	return fileLists
    # atom = {"dirs": root, "dirs": dirs,"files":files }

fileNameAsDate = time.strftime('%Y%m%d',time.localtime(time.time()))

# open file as write mode
f=open(fileNameAsDate+".html","w+")

# html head
f.writelines("<html>\n<head><meta charset=\"utf-8\" /></head>")
f.writelines("<style type=\"text\/css\">a {cursor: copy;text-decoration: none;display: block;border: 1px solid;width: 200px;height: 30px;border-radius: 50px;text-align: center;padding-top: 10px;}")
f.writelines("div{padding-left: 100px;background-color: efc;border-radius: 700px;text-align: center;}</style>")
f.writelines("\n<body>")

files = getAllFiles()[0]['files']

for i in files:
	if ".pdf" in i:
		print(str(i))
		f.writelines("\n <a href='"+str(i)+"'>"+ str(i)+"</a><br>")
f.writelines("\n</body>")
f.close()