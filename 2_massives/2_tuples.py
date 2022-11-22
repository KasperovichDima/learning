"""Tuples."""


"""Tuples as records."""
print('Example of % formating:')
traveler_id = ('USA', '31195855')
print('%s/%s' % traveler_id)


"""Если вы хотите явно узнать, является ли значение кортежа (или вообще лю-
бого объекта) фиксированным, можете воспользоваться встроенной функцией
hash для создания функции fixed вида:"""


def fixed(obj) -> bool:
    """Returns true if object is hashable, false if not."""
    try:
        hash(obj)
        return True
    except TypeError:
        return False


print('Hashable or not tuple demonstration:')
print(fixed((1, 2, 'mama')))
print(fixed((1, 2, ['mama', 'papa'])))


print("Использование * для выборки лишних элементов:")
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


print('\nРаспаковка с помощью * в вызовах функций\
и литеральных последовательностях:')
print(fun(*[1, 2], 3, *range(4, 7)))

"""
Символ * можно также использовать при определении литералов типа list ,
tuple и set , как показано в следующих примерах, взятых из официальной до-
кументации:
"""
*range(4), 4
# (0, 1, 2, 3, 4)
[*range(4), 4]
# [0, 1, 2, 3, 4]
{*range(4), 4, *(5, 6, 7)}
{0, 1, 2, 3, 4, 5, 6, 7}

print('Распаковка вложенных кортежей для доступа к долготе:')

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.3f} | {lon:9.3f}')


"""Каждый кортеж содержит четыре поля, причем последнее - пара координат."""
"""Присваивая последнее поле кортежу, мы распаковываем координаты."""
"""Условие if longitude <= 0: отбирает только мегаполисы в Западном полушарии."""  # noqa: E501

if __name__ == '__main__':
    main()
