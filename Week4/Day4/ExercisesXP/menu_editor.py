import menu_item
import menu_manager

def show_user_menu():
    while True:
        choice = input("\n(V)IEW MENU\n(A)DD AN ITEM\n(D)ELETE AN ITEM\n(U)PDATE AN ITEM\n(S)HOW THE MENU\n(Q)UIT\n--> ").lower()
        if choice == 'v':
            view_item()
        if choice == 'a':
            add_item_to_menu()
        if choice == 'd':
            remove_item_from_menu()
        if choice == 'u':
            update_item_from_menu()
        if choice == 's':
            show_restaurant_menu()
        if choice not in 'vadusq':
            print("Incorrect data\n")
        if choice == 'q':
            show_restaurant_menu()
            print('Bye, bye!')
            break

def view_item():
    item = input("Input an item: ")
    item_output = menu_manager.MenuManager.get_by_name(item)
    print(item_output)

def add_item_to_menu():
    item_name = input("Input the item: ").lower()
    item_price = input("Input it's price:").lower()
    item = menu_item.MenuItem(item_name, item_price)
    try:
        item.save()
        print(f"{item_name} was added succesfully!")
    except Exception:
        print("Some error")

def remove_item_from_menu():
    item_name = input("Input the item: ").lower()
    item = menu_item.MenuItem(item_name, price=None)
    try:
        item.delete()
        print(f"{item_name} was removed succesfully!")
    except Exception:
        print("Some error")

def update_item_from_menu():
    item_name = input("Input the item to update: ").lower()
    new_item_name = input("Input new item: ").lower()
    new_item_price = input("Input new price: ").lower()
    item = menu_item.MenuItem(item_name, price=None)
    try:
        item.update(new_item_name, new_item_price)
        print(f"{item_name} was updated succesfully!")
    except Exception:
        print("Some error")

def show_restaurant_menu():
    menu_manager.MenuManager.all_items()

show_user_menu()

