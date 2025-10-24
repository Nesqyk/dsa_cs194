class Product:

    # Define the con
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell_item(self, quantity):
        if(quantity <= self.stock):
            self.stock -= quantity
            print(f" Nahalin ang {self.name} nahibiling stock: {self.stock}")
        else:
            print(f"{self.name} is currently out of stock, please consider other items")
    
item = Product("Milk", 5000, 10)
item.sell_item(5)