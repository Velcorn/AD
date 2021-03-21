from math import floor


def reverse_list(l):
    for i in range(floor(len(l) / 2)):
        l[i], l[len(l) - i - 1] = l[len(l) - i - 1], l[i]
    return l


if __name__ == '__main__':
    assert reverse_list([x for x in range(1, 10)]) == [x for x in range(1, 10)][::-1]
    assert reverse_list([x for x in range(1, 11)]) == [x for x in range(1, 11)][::-1]
    print("Passed")
