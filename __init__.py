from Board import Board


placeHolder = 0
board = [placeHolder,placeHolder,placeHolder,placeHolder,
placeHolder,placeHolder,placeHolder,placeHolder,
placeHolder,placeHolder,placeHolder,placeHolder,
placeHolder,placeHolder,placeHolder,placeHolder]


new = Board(board)
new.createBoard()
new.listPrint()
userInput = input()

while(userInput != 0):
    if userInput == 'w':
        new.tileUp()
    elif userInput == 's':
        new.tileDown()
    elif userInput == 'a':
        new.tileLeft()
    elif userInput == 'd':
        new.tileRight()
    else:
        print("invalid use WASD")

    new.listPrint()
    userInput = input()
