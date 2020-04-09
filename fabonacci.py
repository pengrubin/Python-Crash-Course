def climb_stair(n):
	if n==1:
		return 1
	elif n==2:
		return 1
	else:
		fabo = climb_stair(n-1)+climb_stair(n-2)
	return fabo

a = climb_stair(10)
print(a)