import abc
from typing import TypeVar


T = TypeVar('T', str, float)


class Validated(abc.ABC):

    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance: object, value: T) -> None:
        value = self.validate(self.storage_name, value)
        instance.__dict__[self.storage_name] = value

    @abc.abstractmethod
    def validate(self, name, value: T) -> T:
        """вернуть проверенное значение или возбудить ValueError."""

 
class Qantity(Validated):
    """check val is > 0"""

    def validate(self, name, value: T) -> T:
        if value <= 0:
            raise ValueError(f'{name} must be > 0')
        return value
    

class NonBlank(Validated):
    """check description is not blank"""

    def validate(self, name, value: T) -> T:
        value = value.strip()
        if not value:
            raise ValueError(f'{name} must not be blank')
        return value


class LineItem:
    description = NonBlank()
    weight = Qantity()
    price = Qantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price
    

# raisins = LineItem('Golden raisins', 10, 6.95)
# st = raisins.subtotal()
# print(st)
# raisins.weight = -20  # trash value
# st = raisins.subtotal()
# print(st)  # trash output
truffle = LineItem(' ', 100, 325)
# truffle = LineItem('White truffle', 100, 325)
print(truffle.subtotal())
