def calc(A, B):
    count = {}
    for e in A:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1
    s = ""
    for i in range(len(B)):
        try:
            if count[i] <= B[i]:
                s += "1"
            else:
                s += "0"
        except KeyError:
            s += "1"
    return s


print(calc([0, 0], [0]))
print(calc([2, 2, 2, 3, 4], [0, 1, 2, 1, 3]))
print(calc([3, 4], [0, 0, 0, 0, 0]))
