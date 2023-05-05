"""Object representations"""
from array import array
import math


class Vector2d:
    """Simple 2d vector class."""

    # typecode – это атрибут класса, которым мы воспользуемся, когда будем пре-
    # образовывать экземпляры Vector2d в последовательности байтов и наоборот.
    typecode = 'd'  # 1

    # Преобразование x и y в тип float в методе __init__ позволяет на ранней ста-
    # дии обнаруживать ошибки, это полезно в случае, когда конструктор Vector2d
    # вызывается с неподходящими аргументами.
    def __init__(self, x, y):
        self.x = float(x) # 2
        self.y = float(y)

    # Наличие метода __iter__ делает Vector2d итерируемым; именно благодаря
    # ему работает распаковка (например, x, y = my_vector ).
    def __iter__(self):
        return (i for i in (self.x, self.y)) # 3

    # Метод __repr__ строит строку, интерполируя компоненты с помощью син-
    # таксиса {!r} для получения их представления, возвращаемого функцией
    # repr ; поскольку Vector2d – итерируемый объект, *self поставляет компоненты
    # x и y функции format .
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) # 4

    # Из итерируемого объекта Vector2d легко построить кортеж для отображения
    # в виде упорядоченной пары.
    def __str__(self):
        return str(tuple(self)) # 5

    # Для генерации объекта типа bytes мы преобразуем typecode в bytes и конкате-
    # нируем…
    # … с объектом bytes, полученным преобразованием массива, который по-
    # строен путем обхода экземпляра.
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + # 6
        bytes(array(self.typecode, self))) # 7

# Для быстрого сравнения всех компонентов мы строим кортежи из операн-
# дов. Это работает, когда операнды являются экземплярами класса Vector2d ,
# но не без проблем. См. предупреждение ниже.
    def __eq__(self, other):
        return tuple(self) == tuple(other) # 8

    # Модулем вектора называется длина гипотенузы прямоугольного треуголь-
    # ника с катетами x и y.
    def __abs__(self):
        return math.hypot(self.x, self.y) # 9

    # Метод __bool__ вызывает abs(self) для вычисления модуля, а затем преоб-
    # разует полученное значение в тип bool , так что 0.0 преобразуется в False ,
    # а любое число, отличное от нуля, – в True.
    def __bool__(self):
        return bool(abs(self)) # 10

    # Метод класса снабжен декоратором classmethod
    @classmethod
    def frombytes(cls, octets):
        # Прочитать typecode из первого байта.
        typecode = chr(octets[0])
        # Создать объект memoryview из двоичной последовательности октетов и при-
        # вести его к типу typecode.
        memv = memoryview(octets[1:]).cast(typecode)
        # Распаковывать memoryview , образовавшийся в результате приведения типа,
        # и получить пару аргументов, необходимых конструктору.
        return cls(*memv)
