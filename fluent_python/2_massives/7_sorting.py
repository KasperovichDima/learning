"""Метод list . sort и встроенная функция sorted"""

"""
Метод list.sort сортирует список на месте, т. е. не создавая копию. Он возвра-
щает None , напоминая, что изменяет объект-приемник 1 , а не создает новый
список.
"""
uns_lst = [5, 7, 3, 0, 9, 6, 8, 1]
print(id(uns_lst))
uns_lst.sort()
print(uns_lst)
print(id(uns_lst))

print('sort() returns None and modify existing object:\n', uns_lst.sort())
print('sorted returns new sorted list:\n', sorted(uns_lst))
print('2 objects have same id:', id(uns_lst) == id(sorted(uns_lst)))

# У соглашения о возврате None в случае обновления на месте
# есть недостаток: такие методы невозможно соединить в цепочку.

"""
встроенная функция sorted создает и возвращает новый
список. На самом деле она принимает любой итерируемый объект в качест­
ве аргумента, в том числе неизменяемые последовательности и генераторы
(см. главу 147). Но независимо от типа исходного итерируемого объекта sorted
всегда возвращает новый список.
"""

# sort and sorted has 2 keys: reverse and key - function.
# Необязательный именованный параметр key можно также ис-
# пользовать совместно с встроенными функциями min() и max()
# и другими функциями из стандартной библиотеки (например,
# itertools.groupby() или heapq.nlargest()).
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits, key=len, reverse=True)
['raspberry', 'banana', 'grape', 'apple']
# Поскольку алгоритм сортировки устойчивый, строки
# равной длины остутса в исходном порядке.

# В отсортированной последовательности поиск производится очень эффективно.
