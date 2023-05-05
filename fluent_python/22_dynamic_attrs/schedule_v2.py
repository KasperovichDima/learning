import inspect
import json
from pathlib import Path


JSON_PATH = Path(__file__).with_name('data.json')


def load(path=JSON_PATH):
    records = {}
    with open(path) as fp:
        raw_data = json.load(fp)
    for collection, raw_records in raw_data['Schedule'].items():
        record_type: str = collection[:-1]
        cls_name = record_type.capitalize()
        # Получить объект с таким именем из глобальной области
        # видимости модуля; если такого объекта нет, получаем Record.
        cls = globals().get(cls_name, Record)
        # Если только что полученный объект – класс,
        # который является подклассом Record, то…
        if inspect.isclass(cls) and issubclass(cls, Record):
            # … связать с ним имя factory . Это означает, что factory может быть
            # произвольным подклассом Record , определяемым переменной record_type.
            factory = cls
        else:
            # В противном случае связать имя factory с Record.
            factory = Record
        for record in raw_records:
            key = f'{record_type}.{record["serial"]}'
            records[key] = factory(**record)

        return records

class Record:
    """
    В закрытом атрибуте класса __index будет храниться
    ссылка на dict , возвращенный методом load.
    """
    _index = None

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} serial={self.serial!r}>'
    
    @staticmethod
    def fetch(key):
        """
        fetch сделан статическим методом, чтобы было понятно, что его действие
        не зависит от экземпляра или класса, от имени которого он вызывается.
        """
        if Record._index is None:
            # Заполнить Record.__index , если необходимо.
            Record._index = load()
        return Record._index[key]
    

class Event(Record):
    """Класс Event расширяет Record."""

    def __repr__(self) -> str:
        """
        Если в экземпляре есть атрибут name, включаем его в строковое представление.
        В противном случае делегируем методу __repr__, унаследованному от Record.
        """
        try:
            return f'<{self.__class__.__name__} serial={self.serial!r}>'
        except AttributeError:
            return super().__repr__()
        
    @property
    def venue(self):
        """
        Свойство venue строит ключ key по атрибуту venue_serial
        и передает его методу класса fetch, унаследованному от Record
        """
        key = f'venue.{self.venue_serial}'
        return self.__class__.fetch(key)
    

event = Record.fetch('event.33950')
print(event)
print(event.venue)
print(event.venue.name)
print(event.venue_serial)
