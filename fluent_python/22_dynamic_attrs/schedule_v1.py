import json
from pathlib import Path


JSON_PATH = Path(__file__).with_name('data.json')


class Record:
    def __init__(self, **kwargs) -> None:
        """
        Стандартная идиома для построения экземпляра, атрибуты которого
        создаются из именованных аргументов (подробности см. ниже).
        """
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        """Использовать поле serial, чтобы построить представление Record."""
        return f'<{self.__class__.__name__} serial={self.serial!r}>'
    
    @staticmethod
    def load(path=JSON_PATH):
        """Метод load в конечном итоге вернет словарь экземпляров Record."""
        records = {}
        with JSON_PATH.open() as fp:
            # Разобрать JSON и вернуть объекты Python: списки, словари, числа и т. д.
            raw_data = json.load(fp)
        # Обойти все четыре списка верхнего уровня:
        # 'conferences', 'events', 'speakers' и 'venues'.
        for collection, raw_records in raw_data['Schedule'].items():
            # speakers становится speaker
            record_type = collection[:-1]
            for raw_record in raw_records:
                # Построить ключ в формате 'speaker.3471'.
                key = f'{record_type}.{raw_record["serial"]}'
                # Создать экземпляр Record и сохранить
                # его в словаре records под ключом key.
                records[key] = Record(**raw_record)
        return records
    

records = Record.load(JSON_PATH)
speaker = records['speaker.3471']
print(speaker)
print(speaker.name)
print(speaker.twitter)
