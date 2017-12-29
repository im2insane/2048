from Board import Board

placeHolder = 0
board = [placeHolder,9,2,placeHolder,
placeHolder,5,placeHolder,2,
3,placeHolder,6,placeHolder,
1,placeHolder,4,placeHolder]



new = Board(board)
new.listPrint()
new.tileLeft()
new.tileRight()
new.tileUp()
new.tileDown()


