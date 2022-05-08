from time import sleep

isXTurn = True
board = [[1, 1, False], [1, 2, False], [1, 3, False],
         [2, 1, False], [2, 2, False], [2, 3, False],
         [3, 1, False], [3, 2, False], [3, 3, False]]
tiles = ['', '', '',
         '', '', '',
         '', '', '']

# Dont new lines so they can see previous moves instead of clearing lines
def clearConsole():  # move to new script
    for i in range(15):
        print("\n")

# print out the board
def printBoard(pos):
    if pos != 0:
        sleep(1)
        clearConsole()
    else:
        print("Welcome To Python TIC-TAC-TOE!\n")

    print("  1   2   3")
    print("1 " + tiles[0] + "\t| " + tiles[1] + "\t| " + tiles[
        2] + "\t")  # make a function from this and move to new script
    print("_______________")
    print("2 " + tiles[3] + "\t| " + tiles[4] + "\t| " + tiles[5] + "\t")
    print("_______________")
    print("3 " + tiles[6] + "\t| " + tiles[7] + "\t| " + tiles[8] + "\t")

# ask user for a position input
def askForPositions():
    if not isXTurn:
        print("O's Turn\n")
    else:
        print("X's Turn\n")
    yPos = input("Enter Board Y-Position (1-3): \n")
    xPos = input("Enter Your X-Position (1-3): \n")
    while (len(xPos) > 1 or len(yPos) > 1 or not xPos.isdigit() or not yPos.isdigit() or
           int(yPos) > 3 or int(yPos) < 1) or (int(xPos) > 3 or int(xPos) < 1):
        clearConsole()
        printBoard(1)
        print("Invalid Input Try again")
        if not isXTurn:
            print("O's Turn\n")
        else:
            print("X's Turn\n")
        yPos = input("Enter Board Y-Position (1-3): \n")
        xPos = input("Enter Your X-Position (1-3): \n")
    return [int(yPos), int(xPos), False]

# checks if tile is taken, if not place an x or o there depending on the turn
def checkIfPositionIsTaken(pos):
    for i in range(9):
        if pos == board[i]:
            print("MATCH")
            board[i] = [pos[0], pos[1], True]
            print(board[i])
            if isXTurn:
                tiles[i] = 'x'
                listOfGlobals = globals()  # only way to assign new values to "Undetermined value" globals
                listOfGlobals['isXTurn'] = False
            elif not isXTurn:
                tiles[i] = 'o'
                listOfGlobals = globals()  # only way to assign new values to "Undetermined value" globals
                listOfGlobals['isXTurn'] = True
            return True
    return False


def checkWinCondition():
    # straight Across Wins
    if tiles[0:3] == ['x', 'x', 'x'] or tiles[0:3] == ['o', 'o', 'o'] or tiles[3:6] == ['x', 'x', 'x'] \
            or tiles[3:6] == ['o', 'o', 'o'] or tiles[6:10] == ['x', 'x', 'x'] or tiles[6:10] == ['o', 'o', 'o']:
        return True
    # down Wins
    if (tiles[0] == tiles[3] and tiles[3] == tiles[6] and tiles[6] != '') or \
            (tiles[1] == tiles[4] and tiles[4] == tiles[7] and tiles[7] != '') \
            or (tiles[2] == tiles[5] and tiles[5] == tiles[8] and tiles[8] != ''):
        return True
    # Diagonal Wins
    if (tiles[0] == tiles[4] and tiles[4] == tiles[8] and tiles[0] != '') or \
            (tiles[2] == tiles[4] and tiles[4] == tiles[6] and tiles[2] != ''):
        return True

    # else game isn't over
    return False

# checks if all tiles are taken up
def checkDrawCondition():
    for i in range(len(tiles)):
        if tiles[i] == '':
            return False
    return True


printBoard(0)
# create gameplay loop
while not checkWinCondition() and not checkDrawCondition():
    checkIfPositionIsTaken(askForPositions())
    printBoard(1)

#Game Over printing
if checkDrawCondition():
    print("GAME OVER! DRAW!")
elif isXTurn:
    print("GAME OVER O Wins")
else:
    print("GAME OVER X Wins")

exit(0)
