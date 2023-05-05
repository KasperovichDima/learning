from typing import Iterator

def fib(stop=100) -> Iterator[int]:
    a, b = 0, 1
    while a < stop:
        yield a
        a, b = b, a + b

for _ in fib(1_000):
    print(_)