import numpy as np
import itertools
from Helper import Helper

class Board:
    def __init__(self,lst):
        self.__len = int(len(lst)**.5)
        self.__board = lst
        self.__board2d = np.array(lst).reshape(self.__len,self.__len)
        self.__helper = Helper()

    def getBoard(self):
        return self.__board

    def getBoard2d(self):
        return self.__board2d

    def __update2dBoard__(self): #2d board is updated with 1d board
        self.__board2d = np.array(self.__board).reshape(self.__len,self.__len)
        print("2d")
        self.__helper.print2DLst(self.__board2d)

    def __updateBoard__(self): #1d board is updated with 2d board
        self.__board = list(itertools.chain(*self.__board2d))
        print("d")
        self.__helper.printLst(self.__board)

    def __tileUp__(self):
        pass




