#_*_coding=utf-8_*_
#__author__='xj'
'mutiple inherance example'

class Animal(object):
	def eat(self):
		print('i can eat, beacous im a animal')

class Bird(Animal):
	def foot(self):
		print('im a bird ,i have two footies')

class FlyAbleMixIn(Animal):
	def fly(self):
		print('i can fly')

class eagle(Bird,FlyAbleMixIn):
	pass
