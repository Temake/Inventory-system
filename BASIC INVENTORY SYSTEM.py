inventory={}

def additem(name,quantity,price):
    if name in inventory:
        inventory[name]=inventory[name]+quantity
    else:
        inventory[name]=quantity
        inventory[price]=price
    return inventory
def removeitem(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed from inventory.")
        return inventory
    else:
        print("Item not in inventory")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        if quantity is not None:
            inventory[name]['quantity'] = quantity
        if price is not None:
            inventory[name]['price'] = price
        print(f"Item '{name}' updated.")
    else:
        print(f"Item '{name}' does not exist. Use 'add_item' to add it.")

