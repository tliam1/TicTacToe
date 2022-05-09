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
    print("\n" * 15)  # no need for a for loop

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

    lines = [
        # --- horizontal ---
        tiles[0:3],
        tiles[3:6],
        tiles[6:9],
        # --- vertical ---
        tiles[0:9:3],
        tiles[1:9:3],
        tiles[2:9:3],
        # --- diagonal ---
        tiles[0:9:4],
        tiles[2:7:2]
        ]
    assert all(len(line) == 3 for line in lines)  # program fails if any line indexes have length > 3
    if any(filled_with_Xs(line) or filled_with_Xs(line) for line in lines):  # Line = lines[i] (or tiles[x:x])
        return True
# The any() function returns True if any element of an iterable is True. If not, it returns False.

    # else game isn't over
    return False

# checks if all tiles are taken up
def checkDrawCondition():
    for i in range(len(tiles)):
        if tiles[i] == '':
            return False
    return True

def filled_with_Os(line):  # I like these declared outside of the scope of another function, more like c++
    return line == ['o', 'o', 'o']  # returns true of an line in lines has a list containing 3 o's
def filled_with_Xs(line):
    return line == ['x', 'x', 'x']  # returns true of an line in lines has a list containing 3 X's


# print(board[0][2]) use this to reference part of a 2D list
printBoard(0)
# create gameplay loop
while not checkWinCondition() and not checkDrawCondition():
    checkIfPositionIsTaken(askForPositions())
    printBoard(1)

# Game Over printing
if checkDrawCondition():
    print("GAME OVER! DRAW!")
elif isXTurn:
    print("GAME OVER O Wins")
else:
    print("GAME OVER X Wins")


exit(0)