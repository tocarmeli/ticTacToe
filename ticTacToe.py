board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
triplets =[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
defaultMovePriorities = [0, 2, 8, 6, 4, 1, 5, 7, 3]
def printBoard():
    for index in range(len(board)):
        if board[index] == ' ':
            print(index, end=" ")
        else:
            print(board[index], end=" ")
        if index % 3 == 2:
            print('')

def checkTripletWin(k, p):
    # k should be 0..8
    # p should be X or O
    if board[triplets[k][0]] == p and board[triplets[k][1]] == p and board[triplets[k][2]] == p:
        return True
    return False

def checkWin(p):
    for k in range(8):
        if checkTripletWin(k, p):
            return True
    return False

def tripletAlmostFull(t, p):
    for k in range(3):
        if board[triplets[t][k]] == ' ' and board[triplets[t][(k + 1) % 3]] == p and board[triplets[t][(k + 2) % 3]] == p:
            return triplets[t][k]
    return -1

def findWinningMove():
    for t in range(len(triplets)):
        k = tripletAlmostFull(t, 'O')
        if k != -1:
            print('Found winning move at: ' + str(k))
            return k
    return -1

def findBlockingMove():
    for t in range(len(triplets)):
        k = tripletAlmostFull(t, 'X')
        if k != -1:
            print('Found blocking move at: ' + str(k))
            return k
    return -1

def findDefaultMove():
    for k in defaultMovePriorities:
        if board[k] == ' ':
            return k
    return -1

def checkEndOfGame():
    if checkWin('X'):
        return 'X'
    if checkWin('O'):
        return 'O'
    for k in range(len(board)):
        if board[k] == ' ':
            return 'S'
    return 'T'

turn = input("Who starts? ") # X or O
while True:
    printBoard()
    if turn == 'X': # player plays
        playerPlace = int(input('Pick a location: '))
        board[playerPlace] = 'X'
        turn = 'O'
    else: # computer plays
        print('Computer plays: ')
        
        # check if there is a winning move
        move = findWinningMove()
        if move == -1:
            # check if there is a blocking move
            move = findBlockingMove()
        

        if move == -1:
            # use default strategy
            move = findDefaultMove()

        if move != -1:
            board[move] = 'O'
        else:
            print('Computer passes')
        turn = 'X'

    gameStatus = checkEndOfGame()
    if gameStatus == 'X' or gameStatus == 'O':
        print(gameStatus + ' won')
        break
    if gameStatus == 'T':
        print('Tie')
        break

printBoard()
print('Game Over')