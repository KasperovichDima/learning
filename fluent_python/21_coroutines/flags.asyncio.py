import asyncio

from httpx import AsyncClient

from old_flags import BASE_URL, save_flag, main


async def download_one(client: AsyncClient, cc: str) -> str:
    """
    download_one должна быть платформенной сопрограммой, чтобы она могла
    вызвать await для сопрограммы get_flag , которая выполняет HTTP-запрос.
    Затем она отображает загруженный флаг и сохраняет изображение.
    """
    img = await get_flag(client, cc)
    save_flag(img, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc

async def get_flag(client: AsyncClient, cc: str) -> bytes:
    """
    Метод get экземпляра httpx.AsyncClient возвращает объект ClientResponse
    который заодно является асинхронным контекстным менеджером.
    """
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    rsp = await client.get(url, timeout=6.1, follow_redirects=True)
    return rsp.read()



def download_many(cc_list: list[str]) -> int:
    """
    Выполнять цикл событий, приводящий в действие объект сопрограммы
    supervisor(cc_list) , пока тот не вернет управление. Эта строка блокирует
    выполнение на все время работы цикла событий. Ее результатом является
    значение, возвращенное supervisor .
    """
    return asyncio.run(supervisor(cc_list))


async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:
        tasks = [download_one(client, cc) for cc in sorted(cc_list)]
        res = await asyncio.gather(*tasks)

        return len(res)


if __name__ == '__main__':
    main(download_many)
