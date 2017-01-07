#-*- coding: utf-8 -*-  
#coding=utf-8
#基本
print 'a'
print ord('a')
print chr(65)
print u'abc'.encode('utf-8')
print u'\u5341\u4e5d\u4e16\u7eaa'.encode('utf-8')
print u''
print 3>2

#if :
if int('1999')<2000:
	print '2000'

#list
listtuple = [1,2,3,4,5,5]
print 'List'
print listtuple
print listtuple[-5] #last no.5
print listtuple[0:3] #index 0~3
print listtuple[-5:]

#list.level up
list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print list2[::5] 	# 5n
print list2[::2]	# 2n

#for
for key in list2:
	print key

#new features, python
autoCreateList = range(1,100)
print u'\u81ea\u52a8\u751f\u6210\u6307\u5b9a\u89c4\u5219\u7684\u6570\u7ec4'
print autoCreateList

#error -> for ':'
#1*1 2*2 3*3 ... pow1~100
L= []
for x in range(1,100):
	L.append(x*x)
print L

#pow(1~100)  %2==0
print [x*x for x in range(1,19) if x % 2 ==0]

#pow(1~12)
print u'\u5e42pow(1~12)'.encode('utf-8')
print [x*x for x in range(1,12)]

#pow()
print u'2\u523050\u6bcf3\u4e2a\u8f93\u51fa\u4e00\u4e2a'
print [j for j in range(2,50,3)]

#zhishu.Prime
print u'\u8d28\u6570Prmie'
maxInt = 1000
noprmes = [j for i in range(2,maxInt) for j in range(i*2,maxInt,i)]
primes  = [x for x in range(2,maxInt) if x not in noprmes]
print primes


print u'\u8f93\u51faABC,xyz\u7684\u7ec4\u5408'
print [m+n for m in 'ABC' for n in 'xyz']

print u'\u904d\u5386\u8f93\u51fa\u6240\u6709\u6587\u4ef6\u540d'
#loop out print os . dir 
import os
print [d for d in os.listdir('.')]


#[] ()
generators =  (i for i in range(1,5))
print generators
print generators.next()
print generators.next()
print generators.next()

#map
print 'MAP'
dictmap = {'jack':17,'lily':27,'bob':37}
print dictmap
print dictmap['jack']
print dictmap.get('ifnull','return this is null')

#set
setvalue  =  set([1,2,5])
print setvalue
setvalue.add(3)
print setvalue
setvalue.add(3)
print setvalue

print abs(-100)
#reference
a = abs 
print a(-100)
print cmp(2,1)

print int('123')
print int(123.856)
print float('886')
print str(123)
print unicode(100)
print bool(1)
print bool(-1)
print bool()



def show_aha(x):
	print 'use function must def first!   "pass" to pass /; to continue .'
	if int(x)>0:
		print 'x>0,x='+x
	else:
		pass
#print u'\u8bf7\u8f93\u5165\u4f60\u7684\u540d\u5b57'
print 'pleas input  a number , must number !'
name = raw_input()
print show_aha(name)



def fun2016(x):
	print 'this function will be do instance of check'
	if not isinstance(x,(int , float)):
		raise TypeError('bad type error')
		a=x+1;
		b=x+2;
	return  a,b


