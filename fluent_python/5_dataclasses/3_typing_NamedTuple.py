"""Типизированные именованные кортежи."""
from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float = 12.57
    reference: str ='WGS84'
    c = 'spam'


print(Coordinate.lat)
# _tuplegetter(0, 'Alias for field number 0')
print(Coordinate.lon)
# _tuplegetter(1, 'Alias for field number 1')
print(Coordinate.__doc__)
# Coordinate(lat, lon, reference)

coord = Coordinate(58.5)

# coord.lat = 58  AttributeError: can't set attribute
# coord.lon = 78.65 AttributeError: can't set attribute
# coord.z = 87.54 AttributeError: 'Coordinate' object has no attribute 'z'
# coord.c = "usefull" AttributeError: 'Coordinate' object attribute 'c' is read-only