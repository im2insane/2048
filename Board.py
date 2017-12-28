import numpy as np

class Board:
    def __init__(self,lst):
        self.__len = int(len(lst)**.5)
        self.__board = lst
        self.__board2d = np.array(lst).reshape(self.__len,self.__len)

    def getBoard(self):
        return self.__board

    def getBoard2d(self):
        return self.__board2d

    def __update2d__(self):
        self.__board2d = self.__board2d = np.array(self.__board).reshape(self.__len,self.__len)

    def __updateBoard__(self):
        return sum(self.__board2d,[])

    def __tileUp__(self):
        pass




