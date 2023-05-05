from array import array
import reprlib
import math


class Vector:

    typecode = 'd'
# В «защищенном» атрибуте экземпляра self._components хранится массив
# array компонента Vector
    def __init__(self, components):
        self._components = array(self.typecode, components)
# Чтобы было возможно итерирование, возвращаем итератор, построенный
# по self._components.
    def __iter__(self):
        return iter(self._components)
# Использовать reprlib.repr() для получения представления self._components
# ограниченной длины (например, array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])).
# Удалить префикс array('d' и закрывающую скобку ) , перед тем как подста-
# вить строку в вызов конструктора Vector .
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))
# Построить объект bytes из self._components .
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
    bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)
# Начиная с версии Python 3.8 метод math.hypot принимает N-мерные точки.
# Раньше я пользовался следующим выражением: math.sqrt(sum(x * x for x in
# self)) .
    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))
# Единственное отличие от написанного ранее метода frombytes – последняя
# строка: мы передаем объект memoryview напрямую конструктору, не распако-
# вывая его с помощью * , как раньше.
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
