for i in range(1, len(A)):
	key = A[i]
	j = i - 1
	print("-> j: {}, key: {}".format(j, key))
	while j >= 0 and A[j] > key:
		A[j + 1] = A[j]
		j -= 1
		print("->->A: {}, i: {}, j: {}".format(A, i, j))
	A[j + 1] = key
	print("->->-> A: {}, i: {}, j: {}, key: {}".format(A, i, j, key))
