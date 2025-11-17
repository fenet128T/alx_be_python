def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added {item}")

        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed {item}")
            else:
                print("Item not found in the list")

        elif choice == "3":
            if shopping_list:
                print("Current shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
