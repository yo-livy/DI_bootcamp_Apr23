from game import Game

def get_user_menu_choice():
    user_choice = input("(P)lay a new game or (S)how scores and (Q)uit: ").lower()
    return user_choice
def print_results():
    print(f"You won {results['won']} times")
    print(f"You lost {results['lost']} times")
    print(f"You drew {results['drew']} times")

results ={"won" : 0, "lost" : 0, "drew" : 0}
def main():
    key = True
    while key:
        menu = get_user_menu_choice()
        if menu in ['p', 's', 'q']:
            key = False
        if menu == "p":
            game = Game()
            results[game.play()] += 1
            main()
        elif menu == "s":
            print_results()
            main()
        elif menu == "q":
            print("Thank you for playing!")
            pass
main()
