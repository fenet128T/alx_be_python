# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("What item would you like to add? ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("No item entered. Nothing added.")

        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
            else:
                print("Current list:", shopping_list)
                item = input("What item would you like to remove? ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed.")
                else:
                    print(f"'{item}' not found in the list.")

        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")

        elif choice == '4':
            print("Goodbye! Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()