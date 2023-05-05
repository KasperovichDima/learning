"""Декораторы в стандартной библиотеке"""
import functools

from d3_simple_decorator import upd_clock


# Запоминание с помощью functools.cache
# @cache() применяется к функции,
# возвращенной декоратором @clock
@functools.cache
@upd_clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))

# output without cache:
# [0.00000069s] fibonacci(0) -> 0
# [0.00000070s] fibonacci(1) -> 1
# [0.00005745s] fibonacci(2) -> 1
# [0.00000038s] fibonacci(1) -> 1
# [0.00000076s] fibonacci(0) -> 0
# [0.00000055s] fibonacci(1) -> 1
# [0.00002707s] fibonacci(2) -> 1
# [0.00004574s] fibonacci(3) -> 2
# [0.00011992s] fibonacci(4) -> 3
# [0.00000033s] fibonacci(1) -> 1
# [0.00000029s] fibonacci(0) -> 0
# [0.00000046s] fibonacci(1) -> 1
# [0.00002810s] fibonacci(2) -> 1
# [0.00004801s] fibonacci(3) -> 2
# [0.00000035s] fibonacci(0) -> 0
# [0.00000060s] fibonacci(1) -> 1
# [0.00002138s] fibonacci(2) -> 1
# [0.00000048s] fibonacci(1) -> 1
# [0.00000052s] fibonacci(0) -> 0
# [0.00000057s] fibonacci(1) -> 1
# [0.00002427s] fibonacci(2) -> 1
# [0.00004458s] fibonacci(3) -> 2
# [0.00008627s] fibonacci(4) -> 3
# [0.00015462s] fibonacci(5) -> 5
# [0.00029443s] fibonacci(6) -> 8
# 8

# output with cache:
# [0.00000085s] fibonacci(0) -> 0
# [0.00000073s] fibonacci(1) -> 1
# [0.00006428s] fibonacci(2) -> 1
# [0.00000103s] fibonacci(3) -> 2
# [0.00008443s] fibonacci(4) -> 3
# [0.00000080s] fibonacci(5) -> 5
# [0.00010889s] fibonacci(6) -> 8
# 8

"""
Декоратор functools.cache на самом деле является простой оберткой вокруг по-
явившейся раньше функции functools.lru_cache , более гибкой и совместимой
с Python 3.8 и более ранними версиями. Least Recently Used.
"""
# var 1
# @functools.lru_cache
# def costly_function(a, b):

# var 2
# @functools.lru_cache()
# def costly_function(a, b):

# В обоих случаях используются параметры по умолчанию, а именно:
# maxsize=128
"""
Для достижения оптимальной производительности
maxsize должен быть степенью 2
@lru_cache(maxsize=2**20)
Если maxsize=None , то логика LRU отключается,
поэтому кеш работает быстрее, но элементы никогда не вытесняются, что мо-
жет привести к перерасходу памяти.

typed=False
Определяет, следует ли хранить элементы разного типа раздельно. Напри-
мер, в конфигурации по умолчанию элементы типа float и integer , признан-
ные равными, хранятся лишь один раз, т. е. вызовы f(1) и f(1.0) приведут
к помещению в кеш только одного элемента. Если typed=True , то такие вы-
зовы приведут к созданию двух разных элементов кеша.
"""

