#_*_coding=utf-8_*_
#__author__='xj'
'__slots__ example'

class Student(object):
	__slots__=('name','age')
	pass

class Kid(Student):
	pass
	
class Teenager(Student):
	__slots__=('interst')
	pass