def recursion(n):
	if n == 1:
		return 1
	else:
		return recursion_tail(1,n)
	
def recursion_tail(m,n):
	if n == 1:
		return m
	return recursion_tail(m * n, n-1)