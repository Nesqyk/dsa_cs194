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
        base_details = super().__str__()
        return f"{base_details}, Warranty: {self.warranty_period} months"

# Step 1, 2, & 3: Create the calculate_tax function
def calculate_tax(item):
    """Calculates an 8% tax on an item's price."""
    return item.price * 0.08

# Step 4: Create a Product and an Electronics object
book = Product("The Art of Code", 1250, 50)
phone = Electronics("Smartphone", 35000, 25, 24)

# Step 5: Call the function for both objects and print the result
print(f"The tax for the {book.name} is: ₱{calculate_tax(book):,.2f}")
print(f"The tax for the {phone.name} is: ₱{calculate_tax(phone):,.2f}")