"""
Перегрузка max

Трудно добавлять аннотации типов к функциям, которые в полной мере за-
действуют мощные динамические средства Python.
"""
from collections.abc import Callable, Iterable
from typing import Protocol, Any, TypeVar, overload, Union


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

T = TypeVar('T')
LT = TypeVar('LT', bound=SupportsLessThan)
DT = TypeVar('DT')

# Константа MISSING –
# это уникальный объект, используемый как специальный маркер. Это значение
# по умолчанию именованного аргумента default= , поэтому max может принимать
# default=None и при этом различать следующие две ситуации.
# 1. Пользователь не задал значение аргумента default= , поэтому оно равно
# MISSING , и max возбуждает исключение ValueError , если first – пустой итери-
# руемый объект.
# 2. Пользователь задал значение default= , быть может None , поэтому max воз-
# вращает это значение, если first – пустой итерируемый объект.

MISSING = object()
EMPTY_MSG = 'max() arg is an empty sequence'

@overload
def custom_max(__arg1: LT, __arg2: LT, *args: LT, key: None = ...) -> LT:
    ...
@overload
def custom_max(__arg1: T, __arg2: T, *args: T, key: Callable[[T], LT]) -> T:
    ...
@overload
def custom_max(__iterable: Iterable[LT], *, key: None = ...) -> LT:
    ...
@overload
def custom_max(__iterable: Iterable[T], *, key: Callable[[T], LT]) -> T:
    ...
@overload
def custom_max(__iterable: Iterable[LT], *, key: None = ...,
default: DT) -> Union[LT, DT]:
    ...
@overload
def custom_max(__iterable: Iterable[T], *, key: Callable[[T], LT],
default: DT) -> Union[T, DT]:
    ...

def custom_max(first, *args, key=None, default=MISSING):
    if args:
        series = args
        candidate = first
    else:
        series = iter(first)
        try:
            candidate = next(series)
        except StopIteration:
            if default is not MISSING:
                return default
            raise ValueError(EMPTY_MSG) from None
    if key is None:
        for current in series:
            if candidate < current:
                candidate = current
    else:
        candidate_key = key(candidate)
        for current in series:
            current_key = key(current)
            if candidate_key < current_key:
                candidate = current
                candidate_key = current_key
    return candidate

# Главное преимущество @overload – максимально точное объявление типа
# возвращаемого значения в соответствии с типами переданных аргументов.
# Мы увидим, как проявляется это преимущество, когда будем рассматривать
# перегруженные варианты max группами по одному или по два.


# Аргументы, реализующие SupportsLessThan, но без задания key и default
# @overload
# def max(__arg1: LT, __arg2: LT, *_args: LT, key: None = ...) -> LT:
# ...
# # ... строки опущены ...
# @overload
# def max(__iterable: Iterable[LT], *, key: None = ...) -> LT:
# ...

res1 = custom_max(1, 2, -3)  # -> Any  возвращает 2
res2 = custom_max(['Go', 'Python', 'Rust'])  # -> Any  возвращает Rust

# Аргумент key задан, аргумент default нет
# @overload
# def max(__arg1: T, __arg2: T, *_args: T, key: Callable[[T], LT]) -> T:
# ...

# @overload
# def max(__iterable: Iterable[T], *, key: Callable[[T], LT]) -> T:
# ...

res3 = max(1, 2, -3, key=abs)  # -> int  возвращает -3
res4 = max(['Go', 'Python', 'Rust'], key=len)  # -> str возвращает 'Python'


# Аргумент default задан, аргумент key нет
# @overload
# def max(__iterable: Iterable[LT], *, key: None = ...,
#   default: DT) -> Union[LT, DT]:
# ...

res5 = max([1, 2, -3], default=0)  # -> int возвращает 2
res6 = max([], default=None)  # -> Any | None возвращает None

# Аргументы key и default заданы
# @overload
# def max(__iterable: Iterable[T], *, key: Callable[[T], LT],
#     default: DT) -> Union[T, DT]:
#         ...

res7 = max([1, 2, -3], key=abs, default=None)  # -> int | None возвращает -3
res8 = max([], key=abs, default=None)  # -> Any | None возвращает None