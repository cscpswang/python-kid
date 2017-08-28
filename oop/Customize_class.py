#_*_coding=utf-8_*_
#__author__='xj'
'Customize Class example'
class Student(object):
	def __init__(self,name):
		self.name=name

class Student1(object):
	def __init__(self,name):
		self.name=name
	
	def __str__(self):
		return 'Student1(%s)'%self.name
	
	__repr__ = __str__

class Fib(object):
	def __init__(self):
		a,b =0,1
	
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if(self.a>100000):
			raise StopIteration()
		else:
			return self.a
	
	def __getitem__(self,n):
		s,k = 1,1
		for i in range(n):
			s,k=k,s+k
		return s

class Student2(object):
	def	__init__(self,name):
		self.name=name
	
	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			return lambda:19
		raise AttributeError('no attribute %s' % attr)
	
	
	
