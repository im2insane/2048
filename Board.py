import numpy as np
import itertools
from Helper import Helper

class Board:
    def __init__(self,lst):
        self.__len = int(len(lst)**.5)
        self.__board = lst
        self.__board2d = np.array(lst).reshape(self.__len,self.__len)
        self.__helper = Helper()

    def listPrint(self):
        self.__helper.printLst(self.__board)

    def getBoard(self):
        return self.__board

    def getBoard2d(self):
        return self.__board2d

    def update2dBoard(self): #2d board is updated with 1d board
        self.__board2d = np.array(self.__board).reshape(self.__len,self.__len)
        print("updated 2D Board")
        self.__helper.print2DLst(self.__board2d)

    def updateBoard(self): #1d board is updated with 2d board
        self.__board = list(itertools.chain(*self.__board2d))
        print("updated Board")
        self.__helper.printLst(self.__board)

    def tileUp(self):
        self.__board = self.__helper.tileUp(self.__board)
        print("moved Tile Up")
        self.update2dBoard()

    def tileDown(self):
        self.__board = self.__helper.tileDown(self.__board)
        print("moved tile down")
        self.update2dBoard()

    def tileRight(self):
        self.__board = self.__helper.tileRight(self.__board)
        print("moved tile right")
        self.update2dBoard()

    def tileLeft(self):
        self.__board = self.__helper.tileLeft(self.__board)
        print("moved tile left")
        self.update2dBoard()




