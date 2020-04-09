def search_matrix(matrix, target):
	n = len(matrix)*len(matrix[0])
	start = 0
	end = n - 1
	while start <= end:
		mid = (start + end) // 2
		if matrix[mid//len(matrix[0])-1][mid%len(matrix[0])-1] == target:
			return True
		elif target < matrix[mid//len(matrix[0])-1][mid%len(matrix[0])-1]:
			end = mid - 1
		else:
			start = mid + 1
	return False






a = search_matrix([
  [1,  3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],5
)
print(a)