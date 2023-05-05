"""
Возвращает неизмененное значение. Для средства проверки типов это служит
сигналом о том, что возвращаемое значение имеет указанный тип, но во время
выполнения мы намеренно ничего не проверяем (хотим, чтобы программа
работала максимально быстро).

На этапе выполнения функция typing.cast не делает абсолютно ничего.
"""
from typing import cast

def find_first_word(a: list[object]) -> str:
    ind = next(ind for ind, _ in enumerate(a) if isinstance(_, str))
    return cast(str, a[ind])


z: str = find_first_word([1,2,3,4])  # mypy think it's ok))