import copy
from typing import Iterable


class Owner:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.name = first_name, last_name
        self.queue = [1, 2, 3, 4, 5]

    @property
    def name(self) -> str:
        return self.__dict__['name']

    @name.setter
    def name(self, full_name: Iterable[str]) -> None:
        self.__dict__['name'] = ' '.join(full_name)

    @property
    def queue(self) -> list[int]:
        return copy.copy(self.__dict__['queue'])

    @queue.setter
    def queue(self, new_queue: list[int]) -> None:
        self.__dict__['queue'] = new_queue


o = Owner('dima', 'kasperovich')
# name = o.name
# print(name)
# name = name[::-1]
# print(o.name)
# o.name = 'olga', 'petrutsi'
# print(o.name)

print(o.queue)
o.queue.reverse()
print(o.queue)
o.queue = [7, 8, 4, 1]
print(o.queue)
