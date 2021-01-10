def in_range(A, a, b):
	count, k = process_array(A)
	if b > k:
		b = k
	if a <= 0:
		return count[b]
	else:
		return count[b] - count[a-1]


def process_array(A):
	count = {}
	k = 0
	for n in A:
		if n in count:
			count[n] += 1
		else:
			count[n] = 1
		if n > k:
			k = n
	count[-1] = 0
	for i in range(k+1):
		if i in count:
			count[i] += count[i-1]
		else:
			count[i] = count[i-1]
	return count, k


A = [1, 1, 2, 3, 5, 8, 9, 4]
print(process_array(A))
print(in_range(A, 1, 10))
print(in_range(A, 0, 9))
print(in_range(A, 1, 9))
