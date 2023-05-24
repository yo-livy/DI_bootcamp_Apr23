
def show_user_menu():
    while True:
        choice = input("(V)IEW MENU\n(A)DD AN ITEM\n(D)ELETE AN ITEM\n(U)PDATE AN ITEM\n(S)HOW THE MENU\n--> ").lower()
        if choice == 'v':
            for i in result:
                print (i)

        if choice == 'a':
                    print('a')
        if choice == 'd':
                    print('d')
        if choice == 'u':
                    print('u')
        if choice == 's':
                    print('s')
        else:
            print("Incorrect data")

show_user_menu()