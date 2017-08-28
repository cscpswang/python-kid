def sum(*args):
	def _f():
		a=0
		for arg in args:
			a = a+arg
		return a
	return _f;
	
def count():
	fs=[];
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs;