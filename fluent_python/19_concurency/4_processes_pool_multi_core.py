import sys
from time import perf_counter
from typing import NamedTuple, TypeAlias
# Стремясь эмулировать threading , пакет multiprocessing предоставляет
# multiprocessing.SimpleQueue , но это метод, связанный с предопределенным эк-
# земпляром низкоуровневого класса BaseContext . Мы должны вызвать этот
# SimpleQueue , чтобы построить очередь, но не можем использовать его в анно-
# тациях типов.
from multiprocessing import Process, SimpleQueue, cpu_count
# В модуле multiprocessing.queues есть класс SimpleQueue , который нужен нам в ан-
# нотациях типов.
from multiprocessing import queues

from prime import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue: TypeAlias = queues.SimpleQueue[int]
ResultQueue: TypeAlias = queues.SimpleQueue[PrimeResult]

def check_number(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)

def worker(jobs: JobQueue, results: ResultQueue) -> None:
    """worker получает очередь подлежащих проверке чисел и
    другую очередь, в которую будет помещать результаты."""
    while n := jobs.get():  # if n is 0 - loop will break
        results.put(check_number(n))
    results.put(PrimeResult(0, False, 0.0))  # finish signal

def start_jobs(
        procs: int, jobs: JobQueue, results: ResultQueue
) -> None:
    """Запустить proc процессов, которые будут выбирать
    данные из очереди jobs и посещать результаты в results ."""
    for n in NUMBERS:
        jobs.put(n)  # add nums to job queue
    for _ in range(procs):  # for every core
        proc = Process(target=worker, args=(jobs, results))  # create child process
        proc.start()  # start proc
        jobs.put(0)  # put 0 from every proc as finish signal


def report(procs: int, results: ResultQueue) -> int:
    """Извлечь и отобразить результаты"""
    checked = procs_done = 0
    while procs_done < procs:  # пока не завершатся все дочерние процессы.
        n, prime, elapsed = results.get()  # Получить один PrimeResult
        # Вызов метода очереди .get() блокирует выполнение
        # до тех пор, пока в очереди не появится элемент.
        if n == 0:  # Если n равно 0, то один процесс завершился; увеличить счетчик procs_done.
            procs_done += 1
        else:
            # В противном случае увеличить счетчик checked (в котором хранится
            # количест­во проверенных чисел) и отобразить результаты.
            checked += 1
            label = 'P' if prime else ' '
            print(f'{n:16} {label} {elapsed:9.6f}')  # print result for each number

    return checked  # count of checked numbers


def main() -> None:
    # Если аргументы в командной строке не заданы, то положить количество
    # процессов равным количеству процессорных ядер, в противном случае
    # создать столько процессов, сколько указано в первом аргументе.
    if len(sys.argv) < 2:
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} processes:')
    t0 = perf_counter()
    jobs: JobQueue = SimpleQueue()
    results: ResultQueue = SimpleQueue()
    start_jobs(procs, jobs, results)
    checked = report(procs, results)
    elapsed = perf_counter() - t0
    print(f'{checked} checks in {elapsed:.2f}s')

if __name__ == '__main__':
    main()
