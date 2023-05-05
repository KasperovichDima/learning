"""С опоставление с экземплярами классов – образцами"""
import typing


x = ...

def do_something_with(x):
    ...

# CORRECT:
match x:
    case float():  # correct way to check var type.
        do_something_with(x)

# INCORRECT:
match x:
    case float:  # ОПАСНО!!!
        do_something_with(x)
# В этом примере case float: сопоставляется с любым субъектом, потому что
# Python рассматривает float как переменную, которая затем связывается с субъ-
# ектом.

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]

def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results

# С образцом City(continent='Asia') сопоставляется любой экземпляр City , в ко-
# тором значение атрибута continent равно 'Asia' , вне зависимости от значений
# других атрибутов.

print(match_asian_cities())
# [City(continent='Asia', name='Tokyo', country='JP'), City(continent='Asia', name='Delhi', country='IN')]

def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(cc)
    return results

# С образцом City(continent='Asia', country=cc) сопоставляются те же азиатские
# города, что и раньше, но теперь переменная cc связана с атрибутом country каж-
# дого экземпляра.

print(match_asian_countries())
# ['JP', 'IN']


# Позиционные классы-образцы
def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia'):
                results.append(city)
    return results

print(match_asian_cities_pos())
# [City(continent='Asia', name='Tokyo', country='JP'), City(continent='Asia', name='Delhi', country='IN')]


# Чтобы собрать в коллекцию значения атрибута country , можно было бы написать:
def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)
    return results

print(match_asian_countries_pos())
# ['JP', 'IN']

# Thats all beacause there is a City.__match_args__ attr:
# >>> ('continent', 'name', 'country')