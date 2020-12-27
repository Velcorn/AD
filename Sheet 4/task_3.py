def wichtel_sort(a, b, c, d, e):
    # Sort a, b and c, d.
    if b < a:
        a, b = b, a
    if d < c:
        c, d = d, c
    # Sort pairs a, b and c, d by larger element.
    if d < b:
        a, b, c, d = c, d, a, b
    # Insert e into a, b, d with knowledge a < b < d.
    if e < b:
        if e < a:
            a, b, c, d, e = e, a, b, d, c
        else:
            a, b, c, d, e = a, e, b, d, c
    else:
        if e < d:
            a, b, c, d, e = a, b, e, d, c
        else:
            a, b, c, d, e = a, b, d, e, c
    # Insert e (former c) into a, b, c, d with knowledge e < d.
    if e < b:
        if e < a:
            a, b, c, d, e = e, a, b, c, d
        else:
            a, b, c, d, e = a, e, b, c, d
    else:
        if e < c:
            a, b, c, d, e = a, b, e, c, d
        else:
            a, b, c, d, e = a, b, c, e, d
    return a, b, c, d, e


if __name__ == '__main__':
    from itertools import permutations
    assert all(list(wichtel_sort(*p)) == sorted(p) for p in permutations(range(5)))
    print("Passed")
