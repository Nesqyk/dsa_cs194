# Parent Class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Item: {self.name}, Price: ₱{self.price:,.2f}, Stock: {self.stock}"

# Child Class
class Electronics(Product):
    def __init__(self, name, price, stock, warranty_period):
        super().__init__(name, price, stock)
        self.warranty_period = warranty_period
        
    def __str__(self):
        # This overrides the parent's __str__ method to add more detail
        base_details = super().__str__()
        return f"{base_details}, Warranty: {self.warranty_period} months"

# Demonstration
book = Product("The Art of Code", 1250, 50)
phone = Electronics("Smartphone", 35000, 25, 24)

product_list = [book, phone]

# The same print() call works for both objects, and each
for product in product_list:
    print(product)