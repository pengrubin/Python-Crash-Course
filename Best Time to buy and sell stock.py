def  max_profit(price_list):
	values = []
	min_number = price_list[0]

	for i in range(len(price_list)):
		if price_list[i]<min_number:
			min_number=price_list[i]
			values.append(0)
		else:
			values.append(price_list[i]-min_number)
	return max(values)

a = max_profit([7, 1, 5, 3, 6, 4])
print(a)