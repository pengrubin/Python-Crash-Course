def climb_stair(n):
	import math
	n = n+1
	sqrt_5 = math.sqrt(5)
	fibo = 1/sqrt_5*(((1+sqrt_5)/2)**n-((1-sqrt_5)/2)**n)
	return fibo

a = int(climb_stair(4))
print(a)