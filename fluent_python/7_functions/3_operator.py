"""Модуль operator"""
from functools import reduce
from operator import mul
from operator import itemgetter


# Вычисление факториала с помощью reduce и operator.mul
def factorial(n):
    return reduce(mul, range(1, n+1))

# Itemgeter is used in keys for sorting for example:

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
# for city in sorted(metro_data, key=lambda fields: fields[1]):
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833))
# ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
# ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
# ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))

"""
Близким родственником itemgetter является функция attrgetter , которая соз-
дает функции для извлечения атрибутов объекта по имени. Если передать
attrgetter несколько имен атрибутов, то она также создаст функцию, возвра-
щающую кортеж значений.
"""