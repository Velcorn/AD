def sort_5_elements_with_7_comparisons(a, b, c, d, e):
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if a < c:
        a, b, c, d = c, d, a, b
    if e < c:
        if d < e:
            d, e = e, d
    else:
        if e < a:
            c, d, e = e, c, d
        else:
            a, c, d, e = e, a, c, d
    if b < d:
        if b < e:
            return b, e, d, c, a
        return e, b, d, c, a
    else:
        if b < c:
            return e, d, b, c, a
        return e, d, c, b, a


print(sort_5_elements_with_7_comparisons(20, 5, 10, 25, 15))
