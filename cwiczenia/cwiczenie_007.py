"""
rekurencja
n! = n(n-1)!
0! = 1

def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n-1)

silnia(5)
"""

def flatten(l):
    result = []

    for element in l:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)

    return result

type([])
isinstance([], list)
assert flatten([]) == []
assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert flatten([1, 2, [3, 4, [5, 6], 7], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert flatten([[[[[[[[[[[[[[[[[[[[[1, [1]]]]]]]]]]]]]]]]]]]]]]) == [1, 1]