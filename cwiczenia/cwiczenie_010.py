"""
Utwórz klasę Circle, która powzwoli na tworzenie obiektów reprezentujących koła
"""
import pytest

class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius # podłoga oznacza, że to jest do użytku wew

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return self.PI * self.radius ** 2

    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Area cannot be negative")
        self.radius = (value / self.PI) ** 0.5

    @property
    def perimeter(self):
        return 2 * self.PI * self.radius

    @perimeter.setter
    def perimeter(self, value):
        self.radius = value / (2 * 3.14)


# pip install pytest
def test_valid_scenarios():
    c = Circle(1)

    assert c.perimeter == 3.14 * 2 * 1
    assert c.area == 3.14 * 1 ** 2

    c.radius = 2
    assert c.perimeter == 3.14 * 2 * 2
    assert c.area == 3.14 * 2 ** 2

    c.area = 3.14 * 16
    assert c.radius == 4

    c.perimeter = 3.14 * 2 * 17
    assert c.radius == 17


def test_invalid_scenarios():
    with pytest.raises(ValueError):
        Circle(-1)

    c = Circle(1)
    with pytest.raises(ValueError):
        c.radius = -10

    with pytest.raises(ValueError):
        c.area = -11

    with pytest.raises(ValueError):
        c.perimeter = -12

