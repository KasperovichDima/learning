import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable): ...

    @abc.abstractmethod
    def pick(self): ...

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)


import random
from collections.abc import Iterable
from typing import TypeVar, Generic


T = TypeVar('T')

# В объявлениях обобщенных классов часто используется множественное
# наследование, поскольку мы должны унаследовать Generic, чтобы объявить
# формальные параметры-типы – в данном случае T.
class LottoBlower(Tombola, Generic[T]):
    # Аргумент items метода __init__ имеет тип Iterable[T] , который превращается
    # в Iterable[int], когда экземпляр объявляется как LottoBlower[int].
    def __init__(self, items: Iterable[T]) -> None:
        self._balls = list[T](items)

    def load(self, items: Iterable[T]) -> None: # Метод load имеет аналогичные ограничения.
        self._balls.extend(items)

    def pick(self) -> T:  # Типом возвращаемого значения T в LottoBlower[int] становится int .
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)

    def loaded(self) -> bool: #
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]: # Наконец, T определяет тип элементов в возвращенном кортеже.
        return tuple(self._balls)

# client code:

# Для создания экземпляра обобщенного класса
# мы передаем ему фактический параметр-тип
machine = LottoBlower[int](range(1, 11))  

first = machine.pick()  # Mypy правильно выводит, что first имеет тип int
remain = machine.inspect()  # … и что remain – кортеж tuple целых чисел.
