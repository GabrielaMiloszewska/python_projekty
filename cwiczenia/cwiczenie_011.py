"""
Zaimplementuj klase Vector - reprezentujaca wektor na plaszczyznie
v = Vector(1, 2)
v2 = Vector(3, 4)
assert v + v2 == Vector(4, 6)
assert v - v2 == Vector(-2, -2)

Masz stworzyć klasę Vector, która:
-reprezentuje wektor na płaszczyźnie (czyli ma x i y)
-pozwala używać operatorów: +, -, *, ==, >
-ma ładną reprezentację tekstową

Czyli chcesz, żeby Python rozumiał coś takiego:
v = Vector(1, 2)
v2 = Vector(3, 4)

v + v2        # dodawanie wektorów
v - v2        # odejmowanie
v * 2         # mnożenie przez liczbę
v == v2       # porównanie
v > v2        # porównanie długości
print(v)      # czytelny napis

To się robi za pomocą metod specjalnych (tzw. dunder methods).
"""

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y # każdy wektor ma współrzędną x i y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})" # reprezentacja napisowa czyli jak się zachowa print(v), gdzie v = Vector(1, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # mnożenie przez liczbę
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # pozwala pisać 2 * v
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # porównanie równości
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # długość wektora
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    # porównanie długości
    def __gt__(self, other):
        return self.length() > other.length()


v = Vector(1, 2)
v2 = Vector(3, 4)

print(v + v2)   # Vector(4, 6)
print(v - v2)   # Vector(-2, -2)
print(v * 2)    # Vector(2, 4)
print(2 * v)    # Vector(2, 4)
print(v == v2)  # False
print(v > v2)   # False