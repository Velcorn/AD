# "Cheat" solution
def expo(a, b, c):
    return pow(a, b, c)


""" 
# Proposed solution
def expo(a, b, c):
    if b == 0:
        return 1 % c
    elif b % 2:
        return (a * expo(a, b-1, c)) % c
    else:
        a = expo(a, b // 2, c) % c
        return (a*a) % c
"""


print(expo(1, 0, 99))
print(expo(2, 1, 99))
print(expo(2, 3, 99))
print(expo(100, 100, 1000000007))
