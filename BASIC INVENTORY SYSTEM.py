inventory = {}

def additem(name, quantity, price):
    if name in inventory:
        inventory[name]['quantity'] += quantity  
    else:
        inventory[name] = {'quantity': quantity, 'price': price}  
    return inventory

def removeitem(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed from inventory.")
    else:
        print(f"Item '{name}' not found in inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for name, details in inventory.items():
            print(f"Item: {name}, Quantity: {details['quantity']}, Price: {details['price']}")

def update_item(name, quantity=None, price=None):
    if name in inventory:
        if quantity is not None:
            inventory[name]['quantity'] = quantity
        if price is not None:
            inventory[name]['price'] = price
        print(f"Item '{name}' updated.")
    else:
        print(f"Item '{name}' does not exist. Use 'additem' to add it.")

def menu():
    while True:
        print("\nInventory System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            additem(name, quantity, price)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            update_item(name, int(quantity) if quantity else None, float(price) if price else None)
        elif choice == '3':
            name = input("Enter item name to delete: ")
            removeitem(name)
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting the inventory system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
