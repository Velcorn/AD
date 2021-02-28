def perrin(n):
    p = [3, 0, 2]
    for i in range(3, n+1):
        p.append(p[i-2] + p[i-3])
    return p[n]


def perrin_space(n):
    a = 3
    b = 0
    c = 2
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    else:
        for i in range(3, n+1):
            d = a + b
            a = b
            b = c
            c = d
        return c


print(perrin_space(20))
