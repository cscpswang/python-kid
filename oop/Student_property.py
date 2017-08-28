#_*_coding=utf-8_*_
#__author__='xj'
'@property example'

class Student(object):
	
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self,value):
		self._birth=value
	
	@property
	def age(self):
		return 2015-self.birth