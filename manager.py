import record as utils

fruit_stock = {}


def add_fruit_stock():
    while True:
        try:
            fruit = input("Enter the fruit name to add: ").strip()
            quantity = int(input("Enter the quantity: ").strip())
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            if fruit in fruit_stock:
                fruit_stock[fruit] += quantity
            else:
                fruit_stock[fruit] = quantity
            print(f"{quantity} units of {fruit} added to stock.")
            utils.log_transaction(f"Added {quantity} units of {fruit}.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid data.")


def view_fruit_stock():
    if not fruit_stock:
        print("Fruit stock is empty.")
    else:
        print("Current fruit stock:")
        for fruit, quantity in fruit_stock.items():
            print(f"{fruit}: {quantity} units")
    utils.log_transaction("Viewed fruit stock.")


def update_fruit_stock():
    while True:
        try:
            fruit = input("Enter the fruit name to update: ").strip()
            if fruit not in fruit_stock:
                raise ValueError(f"{fruit} not found in stock.")
            quantity = int(input("Enter the new quantity: ").strip())
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            fruit_stock[fruit] = quantity
            print(f"Fruit stock updated. {fruit}: {quantity} units")
            utils.log_transaction(f"Updated {fruit} to {quantity} units.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid data.")


def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Add fruit stock")
        print("2. View fruit stock")
        print("3. Update fruit stock")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_fruit_stock()
        elif choice == '2':
            view_fruit_stock()
        elif choice == '3':
            update_fruit_stock()
        elif choice == '4':
            print("Exiting Manager Menu.")
            utils.log_transaction("Exited Manager Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
            utils.log_transaction("Invalid choice in manager menu.")
