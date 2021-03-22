def power_xn(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power_xn(a, b-1)


print(power_xn(2, 3))
print(power_xn(4, 4))
