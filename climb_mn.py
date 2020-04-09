def climb_mn(n,m):
	fibo=0
	if n<0:
		return 0
	elif n<=m:
		fibo = 1<<(n-1)
		return fibo
	else:
		fibos=[]
		for i in range(1,m+1):
			a = climb_mn(n-i,m)
			fibos.append(a)
		return sum(fibos)


a=climb_mn(10,5)
print(a)


