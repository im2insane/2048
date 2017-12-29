from Board import Board
import pygame

placeHolder = 0
board = [2,placeHolder,placeHolder,2,
2,placeHolder,placeHolder,2,
placeHolder,2,placeHolder,2,
4,2,placeHolder,2]



new = Board(board)
new.listPrint()
#new.tileLeft()
new.tileRight()
#new.tileUp()
#new.tileDown()


