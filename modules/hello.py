# _*_ coding: utf-8 _*_

' a test module'

__author__ = 'xj'

import sys

def test():
	args = sys.argv
	print(args)
	
def _test():
	print('i am private method')
	
if __name__ == '__main__':
	test()