'''
# Initial stock: {'apples': 50, 'bananas': 30, 'oranges': 20}

# Check stock of bananas
check_stock(store_inventory, "bananas")
# Expected output: "Current stock of bananas: 30"

# Remove 5 oranges
remove_item(store_inventory, "oranges", 5)
# Expected: {'apples': 60, 'bananas': 30, 'oranges': 15, 'grapes': 15}

# Try to remove too many bananas
remove_item(store_inventory, "bananas", 40)
# Expected output: "Not enough bananas in stock."
# Inventory remains: {'apples': 60, 'bananas': 30, 'oranges': 15, 'grapes': 15}

# Remove all grapes (and optionally remove from dict)
remove_item(store_inventory, "grapes", 15)
# Expected: {'apples': 60, 'bananas': 30, 'oranges': 15} (grapes removed)

# Try to remove a non-existent item
remove_item(store_inventory, "mangoes", 5)
# Expected output: "mangoes not found in inventory."
'''
store_inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 20
}

def add_item(dict_name,fruit_name,quantity):
    if fruit_name not in dict_name:
        dict_name[fruit_name] = quantity
    else:
        dict_name[fruit_name] += quantity
    return f"{quantity} Quantities has been added to {fruit_name} section"
def rem_items(dict_name,fruit_name,quantity):
    if fruit_name not in dict_name:
        print(f"Mentioned {fruit_name} was not there at this moment")
    elif (fruit_name in dict_name) & (dict_name[fruit_name] > quantity):
        dict_name[fruit_name] -= quantity
        print(f"With this removal available Quantity of {fruit_name} is {dict_name[fruit_name]}")
    elif dict_name[fruit_name] < quantity:
        print(f"Available Quantity is less than the Asked Quantity...Sorry for the Inconvenience caused...")

def show_stocks(dict_name,fruit_name = None):
    if fruit_name is None:
        print("Available Stock At this Moment is :")
        for key,values in dict_name.items():
            print (f"{key} : {values}")
    else:
        print(f"Available Stock for {fruit_name} this Moment is :{dict_name[fruit_name]}")

print(store_inventory)
add_item(store_inventory,"grapes",50)
print(store_inventory)
rem_items(store_inventory,"grapes",20)
print(store_inventory)
#rem_items(store_inventory,"grapes",50)
show_stocks(store_inventory)