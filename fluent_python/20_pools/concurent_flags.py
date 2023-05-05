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
    executor.__exit__ вызовет executor.shutdown(wait=True), который блокирует
    выполнение программы до завершения всех потоков.

    Метод map похож на встроенную функцию map с тем исключением, что функ-
    ция download_one конкурентно вызывается из нескольких потоков; он возвра-
    щает генератор, который можно обойти для получения значений, возвра-
    щенных каждой функцией, – в данном случае каждое обращение к
    download_one возвращает код страны.
    """
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(tuple(res))


if __name__ == '__main__':
    main(download_many)
