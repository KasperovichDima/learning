from collections.abc import Iterable, Iterator
from typing import Any, TypeAlias


FieldNames: TypeAlias = str | Iterable[str]


def record_factory(cls_name: str, field_names: FieldNames) -> type[tuple]:
    """Принимаем такие же аргументы, как первые два в collections.namedtuple
    возвращаем type, т. е. класс, который ведет себя как кортеж."""

    # Построить кортеж имен атрибутов, он станет
    # атрибутом __slots__ нового класса.
    slots = parse_identifiers(field_names)

    def __init__(self, *args, **kwargs) -> None:
        """Эта функция станет методом __init__ в новом классе.
        Она принимает позиционные и (или) именованные аргументы"""
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, val in attrs.items():
            setattr(self, name, val)

    def __iter__(self) -> Iterator[Any]:
        """Отдавать значения полей в порядке, определяемом атрибутом __slots__ ."""
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self) -> str:
        """Породить удобное представление, обходя __slots__ и self ."""
        values = ', '.join(f'{name}={value!r}'
                           for name, value
                           in zip(self.__slots__, self))
        cls_name = self.__class__.__name__
        return f'{cls_name}({values})'

    # Построить словарь атрибутов класса.
    cls_attrs = dict(
        __slots__=slots,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__,
    )
    # Построить и вернуть новый класс, вызывая конструктор type.
    return type(cls_name, (object,), cls_attrs)


def parse_identifiers(names: FieldNames) -> tuple[str, ...]:
    if isinstance(names, str):
        # Преобразовать строку names , в которой имена
        # разделены пробелами или запятыми, в список строк.
        names = names.replace(',', ' ').split()

    if not all(_.isidentifier() for _ in names):
        raise ValueError('names must all be valid identifiers')
    return tuple(names)


if __name__ == '__main__':
    Dog = record_factory('Dog', 'name weight owner')
    print(dir(Dog))
    rex = Dog('Rex', 30, 'Bob')
    print(rex)