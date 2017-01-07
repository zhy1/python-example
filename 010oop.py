#-*- coding: utf-8 -*-  
#coding=utf-8



# map
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
#而处理学生成绩可以通过函数实现，比如打印学生的成绩：

def print_score(std):
    print '%s: %s' % (std['name'], std['score'])


print_score(std1);


#oop 
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()