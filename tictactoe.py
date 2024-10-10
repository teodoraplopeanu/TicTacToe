import random

gameBoard = ['   ', '   ', '   ',
            '   ', '   ', '   ',
            '   ', '   ', '   ']

currentPlayer = ' X '
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('---+---+---')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('---+---+---')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))

    if inp >= 1 and inp <= 9 and board[inp - 1] == '   ':
        board[inp - 1] = currentPlayer
    else:
        print("Oops, a player is already in that spot!")


# Check for win or tie
def checkHorizontle(board):
    global winner

    if board[0] == board[1] == board[2] and board[1] != '   ':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '   ':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != '   ':
        winner = board[6]
        return True

    return False

def checkVerticle(board):
    global winner

    if board[0] == board[3] == board[6] and board[3] != '   ':
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '   ':
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '   ':
        winner = board[5]
        return True

    return False


def checkDiag(board):
    global winner

    if board[0] == board[4] == board[8] and board[4] != '   ':
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '   ':
        winner = board[4]
        return True

    return False


def checkTie(board):
    global gameRunning

    if '   ' not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def checkWin(board):
    global gameRunning

    if checkDiag(board) or checkHorizontle(board) or checkVerticle(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False

# Switch the player
def switchPlayer():
    global currentPlayer

    if currentPlayer == ' X ':
        currentPlayer = ' O '
    else:
        currentPlayer = ' X '


# Computer
def computer(board):
    while currentPlayer == ' O ':
        pos = random.randint(0, 8)
        if board[pos] == '   ':
            board[pos] = ' O '
            switchPlayer()


while gameRunning:
    printBoard(gameBoard)
    playerInput(gameBoard)
    checkWin(gameBoard)
    checkTie(gameBoard)
    switchPlayer()
    computer(gameBoard)