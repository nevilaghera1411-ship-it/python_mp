# 7. Write a program to create a list and perform various operations on list using menu.
def list_operations():
    my_list = []
    
    while True:
        print("\n--- List Operations Menu ---")
        print("1. Add element")
        print("2. Remove element")
        print("3. Display list")
        print("4. Sort list")
        print("5. Reverse list")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            item = input("Enter element to add: ")
            my_list.append(item)
            print("Element added.")
        elif choice == '2':
            item = input("Enter element to remove: ")
            if item in my_list:
                my_list.remove(item)
                print("Element removed.")
            else:
                print("Element not found.")
        elif choice == '3':
            print("Current List:", my_list)
        elif choice == '4':
            my_list.sort()
            print("List sorted.")
        elif choice == '5':
            my_list.reverse()
            print("List reversed.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

list_operations()