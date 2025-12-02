# %%
"""Inventory Manager"""

from collections import namedtuple

inventory = []

Item = namedtuple('Item', ['name','quantity','price']) 

# A function that appends item to the inventory
def add_item(name, quantity, price):
    inventory.append(Item(name, quantity, price))

# A function that updates the quantity of a specific item in an inventory
def update_quantity(name, new_quantity):
    for i, item in enumerate(inventory): # runs n number of times
        if item.name == name:
            inventory.pop(i) # constant; Tries to find it I guess then remove that list affecting all of the items in the inventory
            inventory.append(Item(name, new_quantity, item.price))
        else:
            print(f"Item '{name}' not found please try again.")

    # Time Complexity O(n)

# A function that finds the index of a certain item base on their name
def find_item(name) -> int:
    for i, item in enumerate(inventory): # runs n number of times
        if item.name == name:
            return i # constant
        else:
            print(f"Item '{name}' not found please try again.")
            return -1 #constant
# A function that removes a certain item from the 'inventory' list base on their 'name
def remove_item(name):
    index = find_item(name) # run n times
    if(index > -1):
        print(f"Successfully Remove the item '{inventory[index].name}' from the Inventory")
        inventory.pop(index) # runs m times
    # Time Complexity : O(n)

# Displays all of the items in the inventory
def display_inventory():
    if len(inventory) != 0:
        for i, item in enumerate(inventory):
            print(f"----\nItem {i + 1}: \nName: {item.name}\nQuantity: {item.quantity}\nPrice: {item.price}\n")

# Prints out the total number of items in the inventory
def total_items():
    if len(inventory) == 0:
        print( print("There are currently no items in the inventory"))
    else:
        print(f"There are currently {len(inventory)} item/s in the inventory")

        

# Item #1
add_item("Laptop", 10, 10000)
update_quantity("Laptop", 30)

# Tries to update an item that does not exist
update_quantity("Milk", 20)

# Item #2
add_item("Cellphone", 30, 20000)

# Item #3
add_item("Tablet", 10, 20000)

display_inventory()

# Tries to remove an Item that does not exist.
remove_item("Eggnog")
remove_item("Laptop")

display_inventory()
total_items()

# %%
