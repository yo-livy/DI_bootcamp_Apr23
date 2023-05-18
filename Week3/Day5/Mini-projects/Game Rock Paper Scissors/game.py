import random
class Game:
    def __init__(self):
        self.user_item = None
        self.computer_item = None
    def get_user_item(self):
        while True:
            self.user_item = input("Please, choose your item (r)ock / (p)aper / (s)cissors : ").lower()
            if self.user_item not in ['r', 'p', 's']:
                print("Error input")
            else:
                return self.user_item
    def get_computer_item(self):
        self.computer_item = random.choice(["r", "p", "s"])
        return self.computer_item
    def get_game_result(self):
        if self.user_item == self.computer_item:
            return "drew"
        elif (self.user_item == "r" and self.computer_item == "s") or (self.user_item == "p" and self.computer_item == "r") or (self.user_item == "s" and self.computer_item == "p"):
            return "won"
        else:
            return "lost"
    def play(self):
        self.get_user_item()
        self.get_computer_item()
        print(f"You selected {self.user_item}. The computer selected {self.computer_item}. You {self.get_game_result()}.")
        return self.get_game_result()
