from collections.abc import Generator
from collections.abc import Generator
from typing import Union, NamedTuple, TypeAlias


def avg() -> Generator[float, float, None]:
    """
    Эта функция возвращает генератор, который отдает значения типа float,
    принимает значения с помощью метода .send() и не возвращает никакого
    полезного значения
    """
    total = .0
    count = 0
    avg = .0
    # В этом бесконечном цикле сопрограмма будет отдавать
    # средние, пока клиентский код посылает значения.
    while True:
        # Здесь предложение yield используется, чтобы приостановить сопрограмму,
        # отдать результат вызывающей стороне и – впоследствии – получить значе-
        # ние, посланное вызывающей стороной, после чего выполнение бесконечного
        # цикла продолжится.
        term = yield avg
        total += term
        count += 1
        avg = total / count

co = avg()
next(co)  # initialization
print(co.send(10))
print(co.send(20))
print(co.send(50))
co.close()  # close Generator
# co.send(5)  # will raise StopIteration



class Result(NamedTuple):
    count: int  # type: ignore
    avg: float


class Sentinel:
    def __repr__(self) -> str:
        return '<Sentinel>'


SendType: TypeAlias = float | Sentinel


def averager_mk2(verbose: bool = False) -> Generator[None, SendType, Result]:
    """
    В этой сопрограмме тип отдаваемого значения None, потому что она не от-
    дает никаких данных. Она получает данные типа SendType и возвращает кор-
    теж типа Result по завершении.
    """
    total = avg = .0
    count = 0
    while True:
        # Подобное использование yield имеет смысл только в сопрограммах, пред-
        # назначенных для потребления данных. Здесь yield отдает None, но получает
        # term от .send(term).
        term = yield
        if verbose:
            print('received', term)
        if isinstance(term , Sentinel):
            break
        total += term
        count += 1
        avg = total / count
    return Result(count, avg)


STOP = Sentinel()


coro_avg = averager_mk2(True)
next(coro_avg)  # initialization
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
try:
    coro_avg.send(STOP)
except StopIteration as e:
    result = e.value

print(result)