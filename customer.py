import record as utils


def purchase_fruit():
    if not manager.fruit_stock:
        print("Fruit stock is empty. Nothing to purchase.")
        utils.log_transaction("Attempted to purchase fruit but stock is empty.")
        return

    while True:
        try:
            print("Available fruit stock:")
            for fruit, quantity in manager.fruit_stock.items():
                print(f"{fruit}: {quantity} units")

            fruit = input("Enter the fruit name to purchase: ").strip()
            if fruit not in manager.fruit_stock:
                raise ValueError(f"{fruit} not found in stock.")

            quantity = int(input("Enter the quantity to purchase: ").strip())
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            if quantity > manager.fruit_stock[fruit]:
                raise ValueError(
                    f"Insufficient stock. Available quantity of {fruit}: {manager.fruit_stock[fruit]} units")

            manager.fruit_stock[fruit] -= quantity
            if manager.fruit_stock[fruit] == 0:
                del manager.fruit_stock[fruit]

            print(f"Purchased {quantity} units of {fruit}.")
            utils.log_transaction(f"Purchased {quantity} units of {fruit}.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid data.")


def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. View fruit stock")
        print("2. Purchase fruit")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            manager.view_fruit_stock()
        elif choice == '2':
            purchase_fruit()
        elif choice == '3':
            print("Exiting Customer Menu.")
            utils.log_transaction("Exited Customer Menu.")
            break
        else:
            print("Invalid choice. Please try again.")
            utils.log_transaction("Invalid choice in customer menu.")
