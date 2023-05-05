#!/usr/bin/env python3
"""DNS Resolver."""
import asyncio
import socket
from keyword import kwlist

# Задать максимальную длину ключевого слова в доменном имени, посколь-
# ку чем оно короче, тем лучше.
MAX_KEYWORD_LEN = 4


async def probe(domain: str) -> tuple[str, bool]:
    """Функция probe возвращает кортеж, содержащий доменное имя и булево
    значение; True означает, что имя успешно разрешено. Возврат доменного
    имени упрощает отображение результатов. Если мы получили кортеж, значит,
    имя разрешено, в противном случае - нет."""
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main() -> None:  # 5
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{name}.dev'.lower() for name in names)
    # Построить список объектов сопрограмм, вызывая
    # сопрограмму probe с каждым аргументом domain.
    coros = [probe(domain) for domain in domains]
    # asyncio.as_completed – генератор, отдающий переданные ему сопрограммы
    # в порядке их завершения, а не в порядке подачи. Он похож на функцию
    # futures.as_completed
    for coro in asyncio.as_completed(coros):
        # Если coro возбуждала необработанное исключение,
        # то оно будет заново возбуждено в этой точке.
        domain, found = await coro
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    """
    asyncio.run запускает цикл событий и возвращает управление только после
    выхода из него. Это типичный паттерн для скриптов, в которых исполь-
    зуется asyncio : реализовать main как сопрограмму и выполнить ее внутри
    блока if __name__ == '__main__':
    """
    asyncio.run(main())
