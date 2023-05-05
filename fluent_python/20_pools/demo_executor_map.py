from concurrent import futures
from time import sleep, strftime


def display(*args):
    """
    Эта функция печатает переданные ей аргументы,
    добавляя временную метку в формате [HH:MM:SS].
    """
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(sleep_time):
    """
    Функция loiter печатает время начала работы, затем спит n секунд и пе-
    чатает время окончания; знаки табуляции формируют отступ сообщения
    в соответствии с величиной n.
    """
    msg = '{}loiter({}): doinfg nothing for {}s...'
    display(msg.format('\t'*sleep_time, sleep_time, sleep_time))
    sleep(sleep_time)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*sleep_time, sleep_time))
    # loiter возвращает n * 10 , чтобы нагляднее представить результаты.
    return sleep_time * 10


def main():
    display('Script starting...')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    # Передать исполнителю executor пять задач (поскольку есть только три по-
    # тока, сразу начнут выполнение лишь три из них: вызывающие loiter(0) ,
    # loiter(1) и loiter(2) ); это неблокирующий вызов.
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('Waiting for individual results:')
    for num, result in enumerate(results):
        display(f'result {num}, {result}')
        # Обращение к enumerate в цикле for неявно вызывает функцию next(results) ,
        # которая, в свою очередь, вызывает метод _f.result() (внутреннего) будуще-
        # го объекта _f , представляющего первый вызов, loiter(0) . Метод result блоки-
        # рует программу до завершения будущего объекта, поэтому каждая итера-
        # ция этого цикла будет ждать готовности следующего результата.


if __name__ == '__main__':
    main()
