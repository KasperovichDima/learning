"""Обзор построителей классов данных."""
from collections import namedtuple
import typing
import dataclasses


# just use class
class ClassCoordinate:

    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

"""Написание стереотипного кода __init__ очень быстро надоедает,
особенно если в классе атрибутов не два, а больше: каждый придется
упомянуть три раза! И к тому же такой стереотипный код не дает нам
того, чего мы ожидаем от объекта Python:"""

moscow = ClassCoordinate(55.76, 37.62)
print(moscow)
# <__main__.Coordinate object at 0x7f8d29805410>
location = ClassCoordinate(55.76, 37.62)
print(location == moscow)
# False
print((location.lat, location.lon) == (moscow.lat, moscow.lon))
# True


# using namedtuple
NTCoordinate = namedtuple('NTCoordinate', 'lat lon')
print(issubclass(NTCoordinate, tuple))
# True
london = NTCoordinate(55.756, 37.617)
print(london)
# NTCoordinate(lat=55.756, lon=37.617) Полезный метод __repr__
print(london == NTCoordinate(55.756, 37.617))
# True Осмысленный метод __eq__


# usinf typing.NamedTuple
TNTCoordinate = typing.NamedTuple('TNTCoordinate',
                                  [('lat', float), ('lon', float)])
print(issubclass(TNTCoordinate, tuple))
# True
print(typing.get_type_hints(TNTCoordinate))
# {'lat': <class 'float'>, 'lon': <class 'float'>}
# Типизированный именованный кортеж можно построить так же,
# задав поля в виде именованных аргументов:
TNTCoordinate = typing.NamedTuple('TNTCoordinate', lat=float, lon=float)

# В примере 5.2 показан тот же класс Coordinate с двумя атрибута-
# ми float и методом __str__ , который отображает координаты в формате 55.8°N,
# 37.6°E.
class TNTCoordinate(typing.NamedTuple):
    lat: float
    lon: float
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

mexico = TNTCoordinate(12.58, 56.78)
# mexico.lat = 12.78 will rise AttributeError:
print(mexico)
# 12.6°N, 56.8°E


# using dataclass
@dataclasses.dataclass(frozen=True)
class DCCoordinate:
    lat: float
    lon: float
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

la = DCCoordinate(25.98, -87.5)
print(la)
# 26.0°N, 87.5°W


"""
Ключевое различие между этими построителями классов - тот факт, что
collections.namedtuple и typing.NamedTuple строят подклассы tuple , поэтому экземп­
ляры оказываются неизменяемыми. По умолчанию @dataclass порождает из-
меняемые классы. Но декоратор принимает именованный аргумент frozen.
"""

"""Конструирование dict."""
# namedtuple and typing.NamedTuple support ._asdict to be represented as dict.
print(mexico._asdict())
# {'lat': 12.58, 'lon': 56.78}
# And dataclasses support just asdict function:
print(dataclasses.asdict(la))
# {'lat': 25.98, 'lon': -87.5}


"""Получение имен полей и значений по умолчанию."""
# For tuples it can be reached by using ._fields and ._fields_defaults:
print(mexico._fields, mexico._field_defaults)
# ('lat', 'lon') {}
# for dataclasses - using dataclasses.fields function.
print(dataclasses.fields(la))
# long and not usefull output

"""Получение типов полей."""
# Use typing.get_type_hints for it
hints = typing.get_type_hints(mexico)
print(hints)
# {'lat': <class 'float'>, 'lon': <class 'float'>}

"""Конструирование dict."""
# Если дан именованный кортеж x , то вызов x._replace(**kwargs) возвращает новый
# экземпляр, в котором значения некоторых атрибутов изменены в соответ-
# ствии с переданными именованными аргументами. Функция уровня модуля
# dataclasses.replace(x, **kwargs) делает то же самое для экземпляра класса с деко-
# ратором dataclass .
new_mexico = mexico._replace(lat=10, lon=2)
print(new_mexico)
# 10.0°N, 2.0°E
dallas = dataclasses.replace(la, lat=45.8, lon=-87)
print(dallas)
# 45.8°N, 87.0°W

"""Новый класс во время выполнения."""
# Иногда требуется создавать классы данных динамически, во время выполнения.
# Для этого можно использовать синтаксис вызова функции collections.namedtuple,
# поддерживаемый также классом typing.NamedTuple . В модуле dataclasses для той же
# цели имеется функция make_dataclass.

