def quantity(field_name: str) -> property:
    """Getter and setter funcs get cls instance."""

    def qty_getter(instance):
        return instance.__dict__[field_name]
    
    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[field_name] = value
        else:
            raise AttributeError('lower than 0')
        
    return property(qty_getter, qty_setter)



class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
    
raisins = LineItem('Golden raisins', 10, 6.95)
print(raisins.__dict__)