# Main variables (global)
board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]
currentPlayer = "X"
winner = None
gameRunning = True

# --------------------------------------------------
# Board printing func
def printBoard(board):
    print("\nTIC TAC TOE")
    for i in range(9):
        row = ""
        for j in range(36):
            if i==0 or i == 8 or j == 0 or j == 35:
                row += "*"
            elif j == 12 or j == 22:
                row += "|"
            elif (i==3 or i==5) and j in range(4,31):
                row += "-"
            elif (i==2 and j==8):
                row += board[0][0]
            elif (i==2 and j==17):
                row += board[0][1]
            elif (i==2 and j==26):
                row += board[0][2]
            elif (i==4 and j==8):
                row += board[1][0]
            elif (i==4 and j==17):
                row += board[1][1]
            elif (i==4 and j==26):
                row += board[1][2]
            elif (i==6 and j==8):
                row += board[2][0]
            elif (i==6 and j==17):
                row += board[2][1]
            elif (i==6 and j==26):
                row += board[2][2]
            else:
                row += " "
        print(row)

#Player input func
def playerInput(board):
    while True:
        print(f"\nPlayer {currentPlayer}'s turn ... ")
        row = int(input("\nEnter a row (1 - 3): "))
        col = int(input("Enter a column (1 - 3): "))
        if (1 <= row <= 3) and (1 <= col <= 3) and board[row-1][col-1] == " ":
            board[row-1][col-1] = currentPlayer
            break
        else:
            print("Sorry, the spot is not empty")

#check for winning combinations (3 func: horizontal, vertical, diagonal)
def checkHorizontle(board):
    global winner
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
        winner = board[0][0]
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        winner = board[1][0]
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        winner = board[2][0]
        return True
def checkVertical(board):
    global winner
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        winner = board[0][0]
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        winner = board[0][1]
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        winner = board[0][2]
        return True
def checkDiagonal(board):
    global winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winner = board[0][0]
        return True
    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        winner = board[2][0]
        return True

#Win checker func
def checkWin():
    global gameRunning
    if checkHorizontle(board) or checkVertical(board) or checkDiagonal(board):
        print(f"\nThe winner is {winner}!")
        printBoard(board)
        gameRunning = False

#Tie checker func
def checkTie(board):
    global gameRunning
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print("It's a tie!")
        printBoard(board)
        gameRunning = False

#Player switcher func
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# main (gather all functions)
print("Weclome to TIC TAC TOE!")
while gameRunning:
   printBoard(board)
   playerInput(board)
   checkWin()
   checkTie(board)
   switchPlayer()


