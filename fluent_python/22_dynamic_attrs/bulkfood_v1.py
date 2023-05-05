class LineItem:

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    @weight.setter
    def weight(self, val: float):
        if val > 0:
            self.__weight = val
        else:
            raise ValueError("weight can't be < 0")
    

raisins = LineItem('Golden raisins', 10, 6.95)
st = raisins.subtotal()
print(st)
raisins.weight = -20  # trash value
st = raisins.subtotal()
print(st)  # trash output
