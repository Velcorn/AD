def in_range(A, a, b):
	count = process_array(A)
	num = 0
	for i in range(a, b+1):
		if count[i]:
			num += count[i]
	return num


def process_array(A):
	count = {}
	for n in A:
		if n in count:
			count[n] += 1
		else:
			count[n] = 1
	return count


A = [1, 1, 2, 3, 5, 8, 9, 4]
print(in_range(A, 1, 5))
