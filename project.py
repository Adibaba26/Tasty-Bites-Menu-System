def display_menu(menu, prices):
    print("\n----- MENU -----")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]} - Rs {prices[i]}")
    print("----------------")

def display_deals(deals):
    print("\n----- DEALS -----")
    for i in range(len(deals)):
        deal = deals[i]
        print(f"{i + 1}. {deal['name']}: {deal['items']} with {deal['cold_drink']} and {deal['fries']} - Rs {deal['price']}")
    print("----------------")

def update_menu(menu, prices):
    display_menu(menu, prices)
    index = int(input("Enter the index of item to update: ")) - 1
    if 0 <= index < len(menu):
        new_name = input("Enter new item name: ")
        new_price = float(input("Enter new price: Rs "))
        menu[index] = new_name
        prices[index] = new_price
        print("Menu updated successfully!")
    else:
        print("Invalid index.")

def update_deals(deals):
    display_deals(deals)
    index = int(input("Enter the index of deal to update: ")) - 1
    if 0 <= index < len(deals):
        new_name = input("Enter new deal name: ")
        new_item = input("Enter new main item: ")
        new_cold_drink = input("Enter new cold drink: ")
        new_fries = input("Enter new fries: ")
        new_price = float(input("Enter new deal price: Rs "))
        deals[index] = {
            "name": new_name,
            "items": new_item,
            "cold_drink": new_cold_drink,
            "fries": new_fries,
            "price": new_price
        }
        print("Deal updated successfully!")
    else:
        print("Invalid index.")

def customer_menu(menu, prices, deals):
    total_bill = 0
    while True:
        print("\nCustomer Menu:\n1. View Menu\n2. View Deals\n3. Order from Menu\n4. Order from Deals\n5. Checkout")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_menu(menu, prices)
        elif choice == '2':
            display_deals(deals)
        elif choice == '3':
            display_menu(menu, prices)
            order = int(input("Enter the menu item number to order: ")) - 1
            if 0 <= order < len(menu):
                print(f"You ordered: {menu[order]} - Rs {prices[order]}")
                total_bill += prices[order]
            else:
                print("Invalid item number.")
        elif choice == '4':
            display_deals(deals)
            order = int(input("Enter the deal number to order: ")) - 1
            if 0 <= order < len(deals):
                deal = deals[order]
                print(f"You ordered: {deal['name']} - Rs {deal['price']}")
                total_bill += deal['price']
            else:
                print("Invalid deal number.")
        elif choice == '5':
            print(f"\nThank you for your order! Your total bill is: Rs {total_bill}")
            break
        else:
            print("Invalid choice.")

def admin_menu(menu, prices, deals):
    while True:
        print("\nAdmin Menu:\n1. View Menu\n2. View Deals\n3. Update Menu\n4. Update Deals\n5. Exit Admin Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_menu(menu, prices)
        elif choice == '2':
            display_deals(deals)
        elif choice == '3':
            update_menu(menu, prices)
        elif choice == '4':
            update_deals(deals)
        elif choice == '5':
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid choice.")

def main():
    menu = ["Pasta", "Burger", "Pizza", "Shawarma", "Fries", "Juice"]
    prices = [1100, 450, 1700, 200, 150, 200]

    deals = [
        {"name": "Deal 1", "items": "Pizza", "cold_drink": "Cola", "fries": "Fries", "price": 1900},
        {"name": "Deal 2", "items": "Burger", "cold_drink": "Sprite", "fries": "Fries", "price": 1000},
        {"name": "Deal 3", "items": "Shawarma", "cold_drink": "Fanta", "fries": "Fries", "price": 700}
    ]

    print("Welcome to Tasty Bites!")
    user_type = input("Enter 1 for Customer, 2 for Owner: ")

    if user_type == '1':
        customer_menu(menu, prices, deals)
    elif user_type == '2':
        username = input("Enter owner username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "pin":
            admin_menu(menu, prices, deals)
        else:
            print("Invalid admin credentials.")
    else:
        print("Invalid input.")

main()
