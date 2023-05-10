def display_board():
    print("TIC TAC TOE")
    for i in range(7):
        row = ""
        for j in range(28):
            if i==0 or i == 6 or j == 0 or j == 27:
                row += "*"
            elif (i==2 or i==4) and j in range(5,23):
                row += "-"
            elif j == 10 or j == 17:
                row += "|"
            else:
                row += " "
        print(row)

display_board()

def player_input(player):
    print(f"Player {player}'s turn...")
    row = ''
    column = ''
    while row not in [1, 2, 3]:
        row = int(input("Enter row (1, 2 or 3): "))
    while column not in [1, 2, 3] :
        column = int(input("Enter column (1, 2 or 3: "))
    position = (row, column)
    print(position)
    return position
player_input("x")







