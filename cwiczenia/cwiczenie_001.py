"""
mamy liste, np dane = [1, 1, 2, 3, 1, 4, 5, 17, 21, 29]

napisz kod  (bez definiowania funkcji),
ktory z danej listy wybierze liczby pierwsze i zapisze je w nowe liscie
...

nowe_dane == [2, 3, 5, 17, 29]

"""

dane = [1, 1, 2, 3, 1, 4, 5, 17, 21, 29]
nowe_dane = []

for el in dane:
    if el > 1:
        for i in range(2, el):
            if el % i == 0:
                break
        else:
            nowe_dane.append(el)

assert nowe_dane == [2, 3, 5, 17, 29]