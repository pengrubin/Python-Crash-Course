def climb_stair(n):
	import math
	sqrt_5 = math.sqrt(5)
	fibo = 1/sqrt_5*(((1+sqrt_5)/2)**(n+1)-((1-sqrt_5)/2)**(n+1))
	return fibo


a = int(climb_stair(3))
print(a)
