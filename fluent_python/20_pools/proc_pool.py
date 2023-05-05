# Нет нужды импортировать multiprocessing , SimpleQueue и т. д., потому что
# concurrent.futures скрывает все это.

import sys
from concurrent import futures
from time import perf_counter
from typing import NamedTuple

from prime import NUMBERS, is_prime


class PrimeResult(NamedTuple):
    n: int
    flag: bool
    elapsed: float


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def main() -> None:
    # Вместо того чтобы самостоятельно решать, сколько рабочих процессов ис-
    # пользовать, когда их количество в командной строке не задано, мы присва-
    # иваем переменной workers значение None и отдаем решение на усмотрение
    # ProcessPoolExecutor.
    if len(sys.argv) < 2:
        workers = None
    else:
        workers = int(sys.argv()[1])
    # to display number of executors:
    executor = futures.ProcessPoolExecutor(workers)
    actual_workers = executor._max_workers  # type: ignore

    print(f'Checking {len(NUMBERS)} numbers with {actual_workers} processes:')

    t0 = perf_counter()
    numbers = sorted(NUMBERS, reverse=True)
    with executor:  # use like context mngr
        # Вызов executor.map возвращает экземпляры PrimeResult, полученные
        # от функции check , в таком же порядке, как аргументы numbers .
        for n, prime, elapsed in executor.map(check, numbers):
            label = 'P' if prime else ' '
            print(f'{n:16} {label} {elapsed:9.6f}s')

    spent = perf_counter() - t0
    print(f'Total time: {spent:.2f}s')


if __name__ == '__main__':
    main()
