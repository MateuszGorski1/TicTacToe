import random

board = ["-", "-", "-",
"-", "-", "-",
"-", "-", "-"]
currentPlayer ="X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def computer(input):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer(board)

def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] =="-":
        board[inp-1] = currentPlayer
    else:
        print("invalid field, try again")

def checkForWin(board):
    global winner
    if(board[0] == board[1] == board[2] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[3] == board[4] == board[5] and board[3] != "-"):
        winner = board[3]
        return True
    elif (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = board[6]
        return True
    elif (board[0] == board[4] == board[8] and board[0] != "-"):
        winner = board[0]
        return True
    elif (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = board[2]
        return True
    elif (board[0] == board[4] == board[7] and board[0] != "-"):
        winner = board[0]
        return True
    elif (board[1] == board[4] == board[7] and board[1] != "-"):
        winner = board[1]
        return True
    elif (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = board[2]
        return True

def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie!")
        gameRunning = False


def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

while gameRunning:

    printBoard(board)
    playerInput(board)
    if checkForWin(board):
        gameRunning = False
    checkIfTie(board)
    switchPlayer(board)
    computer(board)
    if checkForWin(board):
        gameRunning = False
    checkIfTie(board)
