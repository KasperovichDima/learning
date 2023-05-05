"""О бращение с функцией как с объектом"""

# map keyword:
from typing import Any, Iterable


def factorial(n):
    """возвращает n!"""
    return 1 if n < 2 else n * factorial(n - 1)

print(list(map(factorial, range(11))))
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
# Функции высшего порядка
# Функцией высшего порядка называется функция, которая принимает функцию
# в качестве аргумента или возвращает в качестве значения.
# чтобы отсор­тировать список слов по длине, достаточно передать функцию 
# len в качестве аргумента key

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']

def reverse(word: str) -> str:
    return word[::-1]

print(sorted(fruits, key=reverse))


# lambda
# Особенно удобны анонимные функции в списке аргументов функции высшего порядка.
print(sorted(fruits, key=lambda word: word[::-1]))


# callable() will let us know, if object is callable))
for _ in (fruits, factorial, len, 254):
    print(callable(_))
False
True
True
False

from random import shuffle
class BingoCall:
    def __init__(self, objects: Iterable) -> None:
        self.objects = list(objects)
        shuffle(self.objects)

    def __call__(self) -> Any:
        return self.objects.pop()

gh = BingoCall((1,2,3,4,'mama', 'papa', 10,12,13))
print(gh())
print(gh())
print(gh())
print(gh())
print(gh())
print(gh())
print(gh())
print(gh())
