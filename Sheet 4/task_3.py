def wichtel_sort(a, b, c, d, e):
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if a < c:
        a, c = c, a
        b, d = d, b
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
        else:
            return e, b, d, c, a
    else:
        if b < c:
            return e, d, b, c, a
        else:
            return e, d, c, b, a


if __name__ == '__main__':
    from itertools import permutations

    assert all(list(wichtel_sort(*p)) == sorted(p) for p in permutations(range(5)))
