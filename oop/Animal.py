#_*_ coding=utf-8 _*_
#__author__='xj'
'i m an animal'

class Animal(object):
	def run(self):
		print('Animal is running')
		
class Cat(Animal):
	def run(self):
		print('Cat is running')
		
def __init__():
	if __name__ == '__main__':
		run_twice(Cat())
		
def run_twice(animal):
	animal.run()
	animal.run()
	
__init__()