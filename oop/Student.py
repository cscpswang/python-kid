# _*_ coding:utf-8 _*_
__author__ = 'xiangji'

'oop kid,first'

class Student(object):

	def __init__(self,name,score):
		self.name=name
		self.score=score
		
	def print(self):
		print('name',self.name,'score',self.score)
		
	def grade(self):
		if self.score > 9:
			return 'A'
		elif self.score > 6:
			return 'B'
		else:
			return 'C'

