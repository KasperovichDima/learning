import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path

import httpx
import tqdm  # type: ignore

from flags2_common import main, DownloadStatus, save_flag


DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


async def get_flag(client: httpx.AsyncClient, base_url: str, cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    rsp = await client.get(url, timeout=3.1, follow_redirects=True)
    rsp.raise_for_status()
    return rsp.content


async def download_one(client: httpx.AsyncClient,
                       base_url: str,
                       cc: str,
                       semaphore: asyncio.Semaphore,
                       verbose: bool = False
                       ) -> DownloadStatus:
    """
    Использовать semaphore как асинхронный контекстный менеджер, чтобы
    не блокировать программу целиком; только эта сопрограмма приостанав-
    ливается, когда счетчик семафора обращается в нуль.
    """
    try:
        async with semaphore:
            img = await get_flag(client, base_url, cc)
    except httpx.HTTPStatusError as e:
        rsp = e.response
        if rsp.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found {rsp.url}'
        else:
            raise
    else:
        # Сохранение изображения – операция ввода-вывода. Чтобы избежать блоки-
        # рования цикла событий, функция save_flag выполняется в отдельном потоке.
        await asyncio.to_thread(save_flag, img, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'OK'
    if verbose and msg:
        print(cc, msg)
    return status


async def supervisor(cc_list: list[str],
                     base_url: str,
                     verbose: bool,
                     concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)  # <= concur_req can use this Semaphore
    async with httpx.AsyncClient() as client:
        tasks = [download_one(client, base_url, cc, semaphore, verbose) for cc in sorted(cc_list)]
        # Получить итератор, который будет возвращать объекты сопрограмм по мере их завершения.
        tasks_iter = asyncio.as_completed(tasks)
        if not verbose:
            # Обернуть итератор as_completed генераторной функцией tqdm,
            # чтобы показать индикатор хода выполнения.
            tasks_iter = tqdm.tqdm(tasks_iter, total=len(cc_list))
        error: httpx.HTTPError | None = None # create and init err var
        for coro in tasks_iter:
            try:
                # Ждать завершения сопрограммы для получения результата. Это предложе-
                # ние не приводит к блокированию, потому что as_completed порождает только
                # уже завершившиеся сопрограммы.
                status = await coro
            except httpx.HTTPStatusError as e:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg.format(resp=e.response)
                error = e
            except httpx.RequestError as e:
                error_msg = f'{e}, {type(e)}'.strip()
                error = e
            except KeyboardInterrupt:
                break

            if error:
                status = DownloadStatus.ERROR
                if verbose:
                    # В режиме подробной диагностики извлечь URL-адрес из возникшего
                    # исключения и имя файла, чтобы показать код страны.
                    url = str(error.request.url)
                    cc = Path(url).stem.upper()
                    print(f'{cc} finished with error: {error_msg}')
            counter[status] += 1

    return counter


def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int
                  ) -> Counter[DownloadStatus]: 
    coro = supervisor(cc_list, base_url, verbose, concur_req)
    return asyncio.run(coro)


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
