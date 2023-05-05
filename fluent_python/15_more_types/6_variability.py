"""
Допустим, что в школьной столовой действует правило: разрешено устанав-
ливать только автоматы для розлива соков 1 . Разливать любые напитки не разре-
шается, чтобы не поить детей газировкой, которая запрещена советом школы 2 .
"""
from __future__ import annotations
from typing import TypeVar, Generic


class Beverage:  # Beverage, Juice и OrangeJuice из иерархии типов.
    """Любой напиток."""


class Juice(Beverage):
    """Любой фруктовый сок."""


class OrangeJuice(Juice):
    """Восхитительный сок бразильских апельсинов."""


T = TypeVar('T')


class BeverageDispenser(Generic[T]):  # BeverageDispenser параметризован типом напитка.
    """Автомат, параметризованный типом напитка."""
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage

# # Функция install глобальна на уровне модуля. В ее аннотации типа указано,
# # что допустим только автомат для розлива соков.
def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Установить автомат для розлива фруктовых соков."""


# # Allowed:
juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

# # Not allowed:
beverage_dispenser = BeverageDispenser(Beverage())
install(beverage_dispenser)
# # Автомат, разливающий любой напиток Beverage , недопустим, потому что со-
# # гласно правилам столовой разрешены только автоматы для розлива соков Juice.

# # Удивительно, но этот код тоже недопустим:
orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser)

# Тип инвариантен.


# Ковариантный разливочный автомат:

# Установить covariant=True при объявлении переменной-типа; по соглаше-
# нию суффикс _co в typeshed обозначает ковариантные параметры-типы.
T_co = TypeVar('T_co', covariant=True)


class BeverageDispenserCo(Generic[T_co]):

    # Использовать T_co для параметризации специального класса Generic .
    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage


def install_co(dispenser: BeverageDispenserCo[Juice]) -> None:
    """Установить автомат для розлива фруктовых соков."""

orange_juice_dispenser2 = BeverageDispenserCo(OrangeJuice())
install_co(orange_juice_dispenser2)

# Not allowed:
bev_dispenser = BeverageDispenserCo(Beverage())
install_co(bev_dispenser)

# Это была ковариантность: связь тип–подтип между параметризованными
# автоматами изменяется в том же направлении, что и связь тип–подтип между
# параметрами-типами.


# Контравариантная урна

# Теперь смоделируем правило по установке урн для мусора. Предположим, что
# еда и напитки поставляются в биоразлагаемых упаковках и пищевые отходы
# и одноразовые столовые приборы тоже биоразлагаемые. Урны должны быть
# пригодны для биоразлагаемых отходов.

# Refuse – самый общий тип отходов

# Biodegradable – специальный тип отходов, который со временем
# разлагается микроорганизмами. Некоторые виды отходов не яв-
# ляются биоразлагаемыми

# Compostable – специальный тип биоразлагаемых отходов, который
# можно эффективно превратить в органическое удобрение в ком-
# постном баке или в установке компостирования. Не всякие био-
# разлагаемые отходы являются компостируемыми в смысле наше-
# го определения


# Иерархия типов для отходов: Refuse – самый общий тип, Compostable – самый
# специфичный.
class Refuse:
    """Любые отходы."""

class Biodegradable(Refuse):
    """Биоразлагаемые отходы."""

class Compostable(Biodegradable):
    """Компостируемые отходы."""

# T_contra – принятое по соглашению имя контравариантной переменной-типа.
T_contra = TypeVar('T_contra', contravariant=True)

class TrashCan(Generic[T_contra]):  # TrashCan контравариантен относительно типа отходов.

    def put(self, refuse: T_contra) -> None:
        """Хранить отходы, пока не выгружены."""


def deploy(trash_can: TrashCan[Biodegradable]):
    """Установить урну для биоразлагаемых отходов."""


# Allowed:
bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

# Более общий тип TrashCan[Refuse] допустим, потому что может содержать лю-
# бые типы отходов, в т. ч. Biodegradable . Но TrashCan[Compostable] не годится, потому
# что не может содержать Biodegradable:

# Not Allowed:
compost_can: TrashCan[Compostable] = TrashCan()
deploy(compost_can)