import functools
def log(*text):
	def decorate(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s call %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorate

@log('executor')
def now():
	print('2017-8-5')