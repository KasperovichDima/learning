from concurrent import futures

from flags import save_flag, get_flag, main


def download_one(cc: str) -> str:
    """
    Функция, загружающая одно изображение;
    ее будет исполнять каждый поток.
    """
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

def download_many(cc_list: list[str]) -> int:
    """
    Создать экземпляр ThreadPoolExecutor как контекстный менеджер; метод
    executor.__exit__ вызовет executor.shutdown(wait=True), который блокирует вы-
    полнение программы до завершения всех потоков.

    Метод map похож на встроенную функцию map с тем исключением, что функ-
    ция download_one конкурентно вызывается из нескольких потоков; он возвра-
    щает генератор, который можно обойти для получения значений, возвра-
    щенных каждой функцией, – в данном случае каждое обращение к
    download_one возвращает код страны.
    """
    # Для этой демонстрации мы ограничимся только пятью
    # странами с самой большой численностью населения.
    cc_list = cc_list[:5]
    # Установить значение max_workers равным 3, чтобы можно было
    # следить за ожидающими будущими объектами в распечатке.
    with futures.ProcessPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            # Метод executor.submit планирует выполнение вызываемого объекта
            # и возвращает объект future , представляющий ожидаемую операцию.
            future = executor.submit(download_one, cc)
            # Сохранить каждый будущий объект, чтобы впоследствии
            # его можно было извлечь с помощью функции as_completed.
            to_do.append(future)
            # Вывести сообщение, содержащее код страны и
            # соответствующий ему будущий объект future.
            print(f'{future} scheduled for {cc}')

        # as_completed отдает будущие объекты по мере их завершения.
        for count, future in enumerate(futures.as_completed(to_do), start=1):
            res: str = future.result()  # Получить результат этого объекта future .
            print(f'{future} result is {res!r}')  # Отобразить объект future и результат его выполнения.

        return count


if __name__ == '__main__':
    main(download_many)