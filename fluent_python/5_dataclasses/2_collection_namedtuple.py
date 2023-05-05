"""К лассические именованные кортежи."""
from collections import namedtuple
import json


# как можно было бы определить кортеж для хранения информации о городе.
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
print(tokyo.population)
# 36.933
print(tokyo[1])  # К полям можно обращаться по имени или по номеру позиции.
# JP

san_francisco = City('San Francisco', 'US', 78.433, (41.688722, 192.665267))
print(tokyo > san_francisco)
# True

# Атрибуты и методы именованного кортежа:
print(City._fields)
# ('name', 'country', 'population', 'coordinates')
Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
# _make() строит объект City из итерируемого объекта; конструктор City(*delhi_
# data) делает то же самое.
delhi = City._make(delhi_data)
print(delhi._asdict())
# {'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Coordinate(lat=28.613889, lon=77.208889)}
print(json.dumps(delhi._asdict()))  # ._asdict() полезен для сериализации данных в формате JSON.
# {"name": "Delhi NCR", "country": "IN", "population": 21.935, "coordinates": [28.613889, 77.208889]}


# как определить именованный кортеж Coordinate со значением по умол-
# чанию для поля reference
Coordinates = namedtuple('Coordinates', ('lat lon ref'), defaults=['WGS84'])
print(Coordinates(0, 0))
# Coordinates(lat=0, lon=0, ref='WGS84')
print(Coordinates._field_defaults)
# {'ref': 'WGS84'}
