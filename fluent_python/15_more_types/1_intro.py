import functools
import operator
from collections.abc import Iterable
from typing import overload, Union, TypeVar


T = TypeVar('T')
S = TypeVar('S')  # Эта вторая TypeVar понадобится во второй перегруженной сигнатуре


@overload
# Это сигнатура для простого случая: sum(my_iterable) . Результирующим типом
# может быть T – тип элементов, отдаваемых my_iterable , – или int , если итерируе-
# мый объект пуст, потому что значение параметра start по умолчанию равно 0.
def sum(it: Iterable[T]) -> Union[T, int]: ...


@overload
# Если start задано, то оно может иметь тип S , так что результирующим ти-
# пом является Union[T, S] . Именно поэтому нам и нужна переменная S . Если
# бы мы повторно использовали T , то тип start должен был бы быть таким же,
# как тип элементов Iterable[T] .
def sum(it: Iterable[T], /, start: S) -> Union[T, S]: ...

def sum(it, /, start=0):  # В сигнатуре фактической реализации функции нет аннотаций типов.
    return functools.reduce(operator.add, it, start)

x = sum((1,2,3))  # type x is int
y = sum((1,2,3), start=0.75)  # type y is float