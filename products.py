class Product:
    
    def __init__(self, name, price, quantity) -> None:
        
        self.name = name
        # if name is not str:
        #     raise TypeError
        
        self.price = float(price)
        # if price is not float:
        #     raise TypeError
        # if price <= 0:
        #     raise ValueError
        
        self.quantity = int(quantity)
        # if quantity is not int:
        #     raise TypeError
        # if quantity <= 0:
        #     raise ValueError
        
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity
            
    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            deactivate()
    
    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f'{self.name}, Price:{self.price}, Quantity:{self.quantity}'
    
    def buy(self, quantity) -> float:
        if self.quantity - quantity < 0:
            raise ValueError
        else:
            self.quantity -= quantity

        return self.price * quantity

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()