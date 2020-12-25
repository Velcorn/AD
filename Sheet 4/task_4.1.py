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
	for i in range(k, -1, -1):
		for j in range(-1, i):
			if i not in count:
				count[i] = 0
			if j in count:
				count[i] += count[j]
	return count, k


A = [1, 1, 2, 3, 5, 8, 9, 4]
print(in_range(A, 1, 5))
