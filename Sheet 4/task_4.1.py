def in_range(C, k, a, b):
	if b > k:
		b = k
	if a <= 0:
		return C[b]
	else:
		return C[b] - C[a-1]


def process_array(A):
	# Get k.
	k = 0
	for n in A:
		if n > k:
			k = n
	# Get count of each array element and largest array element.
	count = [0]*(k+1)
	for n in A:
		count[n] += 1
	# Get count of elements from 0 to n for every element n.
	for i in range(1, k+1):
		count[i] += count[i-1]
	return count, k


A = [1, 1, 2, 3, 5, 8, 9, 4]
C, k = process_array(A)
print(process_array(A))
print(in_range(C, k, 1, 10))
print(in_range(C, k, 0, 9))
print(in_range(C, k, 1, 9))
