def calc(A, B):
    count = {}
    for e in A:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1
    s = ""
    for i in range(len(B)):
        if i in count:
            if count[i] <= B[i]:
                s += "1"
            else:
                s += "0"
        else:
            s += "1"
    return s


print(calc([0, 0], [0]))
print(calc([2, 2, 2, 3, 4], [0, 1, 2, 1, 3]))
print(calc([3, 4], [0, 0, 0, 0, 0]))
