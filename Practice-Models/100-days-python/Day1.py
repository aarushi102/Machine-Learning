# todo.py

# Function to display the menu
def display_menu():
    print("\n==== To-Do List Menu ====")
    print("1. Add a to-do item")
    print("2. View to-do list")
    print("3. Mark an item as done")
    print("4. Remove an item")
    print("5. Exit")

# Function to add a to-do item
def add_todo(todo_list):
    item = input("Enter the to-do item: ")
    todo_list.append({"task": item, "done": False})
    print("To-do item added.")

# Function to view the to-do list
def view_todo(todo_list):
    print("\n==== To-Do List ====")
    for index, todo in enumerate(todo_list, start=1):
        status = "Done" if todo["done"] else "Pending"
        print(f"{index}. [{status}] {todo['task']}")

# Function to mark an item as done
def mark_done(todo_list):
    view_todo(todo_list)
    choice = int(input("Enter the number of the item to mark as done: "))
    todo_list[choice - 1]["done"] = True
    print("To-do item marked as done.")

# Function to remove an item
def remove_item(todo_list):
    view_todo(todo_list)
    choice = int(input("Enter the number of the item to remove: "))
    del todo_list[choice - 1]
    print("To-do item removed.")

def main():
    todo_list = []

    while True:
        display_menu()
        option = input("Enter your choice: ")

        if option == '1':
            add_todo(todo_list)
        elif option == '2':
            view_todo(todo_list)
        elif option == '3':
            mark_done(todo_list)
        elif option == '4':
            remove_item(todo_list)
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
