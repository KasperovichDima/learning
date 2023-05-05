"""С опоставление с последовательностями - образцами."""


class Robot:
    """
    Just some abstaract robot.
    В зависимости от команды и от количества аргументов
    выполняется тот или иной метод.
    """

    def handle_command(self, msg: str) -> None:
        """Handle robot commands."""

        match msg:
            case ['BEEPER', freq, times]:
                self.beep(times, freq)
            case ['NECK', angle]:
                self.rotate_neck(angle)
            case ['LED', ident, intensity]:
                self.leds(ident, intensity)
            case ['LED', ident, red, green, blue]:
                #  We get here depending on arg count.
                self.leds[ident].set_color(ident, red, green, blue)
            case _:
                raise AttributeError

    def beep(self, freq, times):
        ...

    def rotate_neck(self, angle):
        ...

    def leds(self, ident, intensity):
        ...

########################################


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat: 9.4f} | {lon: 9.4f}')


main()


"""Экземпляры классов str, bytes и bytearray не считаются после-
довательностями в контексте match/case. Субъект match, принад-
лежащий одному из этих типов, трактуется как «атомарное»
значение. Если вы хотите
рассматривать объект одного из этих типов как субъект последо-
вательности, то преобразуйте его тип во фразе match. Например,
так мы поступили с tuple(phone) в следующем фрагменте:
"""
#  match tuple(phone):
#      case ['1', *rest]:  # Северная Америка и страны Карибского бассейна
#          ...
#      case ['2', *rest]:  # Африка и некоторые другие территории
#          ...
#      case ['3' | '4', *rest]:  # Европа
#          ...

"""
С последовательностями-образцами совместимы следующие типы из стан-
дартной библиотеки:
list			 memoryview
tuple		 range
array.array
collections.deque
"""

"""
Символ _ в образцах имеет специальный смысл: он сопоставляется с одним
любым элементом в этой позиции, но никогда не связывается со значением
сопоставленного элемента. Кроме того, _ – единственная переменная, которая
может встречаться в образце более одного раза.
"""

#  Любую часть образца можно связать с переменной с помощью ключевого
#  слова as :
#  case [name, _, _, (lat, lon) as coord]:

print('\n')
cars = [
    ('Ford', 'Sierra', 1988, 2.0, 'sedan'),
    ('Toyota', 'Civic', 2005, 1.4, 'universal'),
    ('Opel', 'Insignia', 2008, 2.0, 'sedan'),
    ('Tank T-72', 1975, '12 + turbine')
]

#  Образцы можно сделать более специфичными, добавив информацию о типе:

#  case [str(name), _, _, (float(lat), float(lon))]:

#  в контексте образца эта синтаксическая конструкция
#  производит проверку типа во время выполнения.


for car in cars:
    match car:
        case [str(brand), str(model), int(year),
              float(volume), str(type) as body_type]:
            print('correct car', body_type)
        case _:
            print('car error!')


"""
С другой стороны, если мы хотим произвести сопоставление произвольной
последовательности-субъекта, начинающейся с str и заканчивающейся вло-
женной последовательностью из двух float , то можем написать:
"""
#  case [str(name), *_, (float(lat), float(lon))]:
"""
Здесь *_ сопоставляется с любым числом элементов без привязки их к пере-
менной. Если вместо *_ использовать *extra , то с переменной extra будет связан
список list , содержащий 0 или более элементов.

Необязательное охранное условие, начинающееся со слова if , вычисляется
только в случае успешного сопоставления с образцом. При этом в условии мож-
но ссылаться на переменные, встречающиеся в образце.
"""
#  case [name, _, _, (lat, lon)] if lon <= 0:
