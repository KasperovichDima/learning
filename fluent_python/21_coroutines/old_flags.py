import time
from pathlib import Path
from typing import Callable

import httpx


# list of county codes to download flags.
POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'https://www.fluentpython.com/data/flags'

DEST_DIR = Path('downloaded')

def save_flag(img: bytes, filename: str) -> None:
    """
    Скопировать img (последовательность байтов)
    в файл с именем filename в каталоге DEST_DIR .
    """
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    """
    Зная код страны, построить URL-адрес и загрузить
    изображение; вернуть двоичное содержимое ответа.
    """
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    # Считается правильным добавлять разумный тайм-аут для сетевых
    # операций, чтобы избежать ненужной блокировки на несколько минут.
    rsp = httpx.get(url, timeout=6.1, follow_redirects=True)  # По умолчанию HTTPX не выполняет перенаправление
    # В этом скрипте нет обработки ошибок, но данный метод возбуждает ис-
    # ключение, если состояние HTTP не принадлежит диапазону 2XX. Это реко-
    # мендуемая практика, позволяющая избежать «немых» отказов.
    rsp.raise_for_status()
    return rsp.content

def download_many(cc_list: list[str]) -> int:
    """
    download_many – основная функция, позволяющая
    провести сравнение с кон-курентными реализациями.

    Обойти список стран в алфавитном порядке, чтобы порядок отображения
    на выходе был такой же, как на входе; вернуть количество загруженных
    изображений.
    """
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ', flush=True)
    return len(cc_list)

def main(downloaded: Callable[[list[str]], int]) -> None:
    # Создать каталог DEST_DIR , если необходимо;
    # не возбуждать исключение, если каталог уже существует.
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloaded(POP20_CC)
    elapsed = time.perf_counter() - t0
    # Аргумент flush=True необходим, потому что по умолчанию
    # Python буферизует выходные строки, т. е. напечатанные
    # символы отображаются только после вывода символа перевода
    # строки.
    print(f'\n{count} downloaded in {elapsed:.2f}s')

if __name__ == '__main__':
    main(download_many)

# Отметим, что функция download_one из примера 20.3, по сути дела, является
# телом цикла for в функции download_many из примера 20.2. Это типичный ре-
# факторинг, встречающийся при написании конкурентного кода: преобразо-
# вать тело последовательного цикла for в функцию, которая будет вызываться
# конкурентно.