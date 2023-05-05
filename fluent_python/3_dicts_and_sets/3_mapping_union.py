"""Объединение отображений оператором |"""


d1 = {'a': 1, 'b': 3, 'e': 15}
d2 = {'a': 2, 'b': 4, 'c': 6}
print(d1 | d2)
# {'a': 2, 'b': 4, 'e': 15, 'c': 6}


d1 |= d2
print(d1)
# содержимое d1 изменилось
# {'a': 2, 'b': 4, 'e': 15, 'c': 6}