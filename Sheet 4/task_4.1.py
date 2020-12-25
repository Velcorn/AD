def in_range(A, a, b):
	count, k = process_array(A)
	print(count, k)
	if b > k:
		b = k
	if a <= 0:
		return count[b]
	else:
		return count[b] - count[a-1]


def process_array(A):
	k = 0
	for n in A:
		if n > k:
			k = n
	count = [[0]*len(A)]*k
	for i in range(len(A)-1):
		for j in range(k-1):
			count[i][j] = 0 if i == 0 else count[i-1][j]
		count[i][A[i]] += 1
	return count, k


A = [1, 1, 2, 3, 5, 8, 9, 4]
print(in_range(A, 1, 5))
