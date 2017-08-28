def iter():
	n=2
	while(true)
		yield n
		n = n+1

def _divisible(n):
	return lambda x : x % n >0
	
def prime():
	