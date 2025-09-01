
# An activity that demonstates inheritance
class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell_item(self, quantity):
        if(quantity <= self.stock):
            self.stock -= quantity
            print(f": {self.stock}")
        else:
            print(f"{self.name} is currently out of stock, please consider other items")
    
item = Product("Milk", 5000, 10)
item.sell_item(5)


class ElectronicsProject(Product):

    def __init__(self, name, price, stock, warranty_period):
        super().__init__(name, price, stock)
        self.warranty_period = warranty_period
    
