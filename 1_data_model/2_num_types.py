"""
__repr__, __abs__, __bool__, __add__, __mul__

vector2d.py: упрощенный класс, демонстрирующий некоторые специальные методы.
Упрощен из дидактических соображений. Классу не хватает правильной
обработки ошибок, особенно в методах ``__add__`` and ``__mul__``.
Далее в книге этот пример будет существенно расширен.
Сложение::
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)
Абсолютная величина::
>>> v = Vector(3, 4)
>>> abs(v)
5.0
Умножение на скаляр::
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0
"""
from __future__ import annotations

import math


class Vector:
    """Vector class."""
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
