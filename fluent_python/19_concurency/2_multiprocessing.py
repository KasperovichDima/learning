"""First examples."""
import itertools
import time
from multiprocessing import Process, Event  # 1
from multiprocessing import synchronize  # 2


def spin(msg: str, done: synchronize.Event) -> None:  # 3
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.15):
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin,  # 4
                      args=('thinking!', done))
    print(f'spinner object: {spinner}')  # 5
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()


# 1
# Базовый API multiprocessing имитирует API threading , но аннотации типов
# и Mypy выявляют различие: multiprocessing.Event – функция (а не класс, как
# threading.Event ), которая возвращает synchronize.Event …

# 2
# … что вынуждает нас импортировать multiprocessing.synchronize …

# 3
# … чтобы записать эту аннотацию типа.

# 4
# Простое использование класса Process похоже на Thread .

# 5
# Объект spinner отображается как <Process name='Process-1' parent=14868 initial> ,
# где 14868 – идентификатор процесса Python, в котором исполняется скрипт
# spinner_proc.py.
