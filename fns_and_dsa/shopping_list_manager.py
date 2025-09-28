
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
            while True:
                item = input("enter an item or enter ** to exit: ")
                if item == "**":
                    break
                else:
                    shopping_list.append(item)
        elif choice == "2":
            while True:
                item = input("Enter an item to remove or enter ** to exit: ")
                if item == "**":
                    break
                elif item in shopping_list:
                    shopping_list.remove(item)
                else:
                    print("item not in shopping list")
        elif choice == "3":
            print(shopping_list)

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()