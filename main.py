import manager
import customer
import record as utils

def main_menu():
    while True:
        print("\nSelect Role:")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            manager.manager_menu()
        elif choice == '2':
            customer.customer_menu()
        elif choice == '3':
            print("Exiting.")
            utils.log_transaction("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            utils.log_transaction("Invalid choice in main menu.")

if __name__ == "__main__":
    main_menu()
