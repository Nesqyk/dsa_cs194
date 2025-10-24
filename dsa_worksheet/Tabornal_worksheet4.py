# Problem 1: Encapsulation & Abstraction


# %%

class Employee:
    """Represents an employee with a name and salary."""
    def __init__(self, name, salary: float):
        self.name = name
        self.salary = salary

    def get_annual_salary(self) -> float:
        return self.salary * 12
    
    def give_raise(self, raise_amount: float):
        self.salary += raise_amount 

    def __str__(self) -> str:
        return f"Name: {self.name}, Salary: {self.salary}, Annual Salary: {self.get_annual_salary()}"

sample_employee = Employee("Tyrone Tabornal", 2000)
print(sample_employee)

sample_employee.give_raise(raise_amount=3000)
print(sample_employee)


# Problem 2: Inheritance
class Vehicle:
    """A base class for different types of vehicles."""
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
    
    def get_info(self) -> str:
        return f"This is a {self.make} {self.model}"
    
class Car(Vehicle):
    """A car, which is a specific type of Vehicle."""
    def __init__(self, make, model, num_doors) -> None:
        super().__init__(make, model)
        self.num_doors = num_doors

honda = Car("Honda", "Civic", 4)
print(honda.get_info())


# Problem 3: Polymorphism
import math

class Shape:
    """A base class for geometric shapes."""
    def get_area(self):
        return 0
    
class Rectangle(Shape):
    """A rectangle, defined by a width and height."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Circle(Shape):
    """A circle, defined by a radius."""
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self) -> float:
        return math.pi * math.pow(self.radius, 2)

_rectangle = Rectangle(120, 30)
_circle = Circle(7)

shapes_list = [_rectangle, _circle]

# Polymorphism: Calling the same .get_area() method on different shape objects.
for shape in shapes_list:
    print(shape.get_area())


# Problem 4: Putting it All Together
class Account:
    """A general bank account with an owner and balance."""
    def __init__(self, owner: str , balance: float):
        self.balance = balance
        self.owner = owner
    
    def deposit(self, amount: float):
        self.balance += amount

class SavingsAccount(Account):
    """A special type of account that earns interest."""
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Increases the balance by the interest rate
        self.balance += (self.balance * self.interest_rate)

def display_account_info(account: Account):
    """Displays owner and balance for any Account object."""
    print(f"{account.owner}'s Account:\nBalance: {account.balance:,.2f}")

sample_account = Account("Tyrone Tabornal", 50000.32)
sample_savings = SavingsAccount("Jane Doe", 40000.32, 0.05) # 5% interest rate

# Polymorphism: The same function works for both Account and SavingsAccount.
display_account_info(sample_account)
display_account_info(sample_savings)
# %%
