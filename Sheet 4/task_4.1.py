def in_range(A, a, b):
	return len([n for n in A if a <= n <= b])


A = [1, 1, 2, 3, 5, 8, 9, 4]
# print(in_range(A, 1, 5))


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
	return count


print(process_array(A))
