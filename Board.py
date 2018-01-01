import numpy as np
import itertools
from Helper import Helper
import random

class Board:
    def __init__(self,lst):
        self.__len = int(len(lst)**.5)
        self.__board = lst
        self.__board2d = np.array(lst).reshape(self.__len,self.__len)
        self.__helper = Helper()

    def listPrint(self):
        self.__helper.printLst(self.__board)

    def addNum(self):
        lst = self.__board
        avaiable_slots = []
        for i in range(0,len(lst)):
            if lst[i] == 0:
                avaiable_slots.append(i)
        rand = random.randint(0,len(avaiable_slots)-1)

        if len(avaiable_slots) == 0:
            pass

        lst[avaiable_slots[rand]] = 2
        self.__board = lst
        self.update2dBoard()

    def createBoard(self):
        self.addNum()
        self.addNum()

    def getBoard(self):
        return self.__board

    def getBoard2d(self):
        return self.__board2d

    def update2dBoard(self): #2d board is updated with 1d board
        self.__board2d = np.array(self.__board).reshape(self.__len,self.__len)
        self.__helper.printStatement("updated 2Dboard")
        #self.__helper.print2DLst(self.__board2d)

    def updateBoard(self): #1d board is updated with 2d board
        self.__board = list(itertools.chain(*self.__board2d))
        self.__helper.printStatement("updated Board")
        #self.__helper.printLst(self.__board)

    def calcUp(self):
        lst = self.__board2d
        self.__helper.printStatement("calc up")
        for i in range(1,len(lst)):
            for j in range(0,len(lst)):
                if(lst[i-1][j] == lst[i][j] and lst[i-1][j] != 0 and lst[i][j] != 0):
                    lst[i-1][j] = lst[i][j]*2
                    lst[i][j] = 0
        self.__board2d = lst
        self.updateBoard()
        self.__board = self.__helper.tileUp(self.__board)
        self.update2dBoard()
        self.addNum()

    def calcDown(self):
        lst = self.__board2d
        self.__helper.printStatement("calc down")
        for i in range(2,-1,-1):
            for j in range(0,len(lst)):
                if(lst[i+1][j] == lst[i][j] and lst[i+1][j] != 0 and lst[i][j] != 0):
                    lst[i+1][j] = lst[i][j]*2
                    lst[i][j] = 0
        self.__board2d = lst
        self.updateBoard()
        self.__board = self.__helper.tileDown(self.__board)
        self.update2dBoard()
        self.addNum()

    def calcLeft(self):
        lst = self.__board2d
        self.__helper.printStatement("calc left")
        for i in range(0,len(lst)):
            for j in range(1,len(lst)):
                if(lst[i][j-1] == lst[i][j] and lst[i][j-1] != 0 and lst[i][j] != 0):
                    lst[i][j-1] = lst[i][j]*2
                    lst[i][j] = 0
        self.__board2d = lst
        self.updateBoard()
        self.__board = self.__helper.tileLeft(self.__board)
        self.update2dBoard()
        self.addNum()

    def calcRight(self):
        lst = self.__board2d
        self.__helper.printStatement("calc right")
        for i in range(0,len(lst)):
            for j in range(2,-1,-1):
                if(lst[i][j+1] == lst[i][j] and lst[i][j+1] != 0 and lst[i][j] != 0):
                    lst[i][j+1] = lst[i][j]*2
                    lst[i][j] = 0
        self.__board2d = lst
        self.updateBoard()
        self.__board = self.__helper.tileRight(self.__board)
        self.update2dBoard()
        self.addNum()

    def tileUp(self):
        self.__board = self.__helper.tileUp(self.__board)
        self.__helper.printStatement("moved tile up")
        self.update2dBoard()
        self.calcUp()

    def tileDown(self):
        self.__board = self.__helper.tileDown(self.__board)
        self.__helper.printStatement("moved tile down")
        self.update2dBoard()
        self.calcDown()

    def tileRight(self):
        self.__board = self.__helper.tileRight(self.__board)
        self.__helper.printStatement("moved tile right")
        self.update2dBoard()
        self.calcRight()

    def tileLeft(self):
        self.__board = self.__helper.tileLeft(self.__board)
        self.__helper.printStatement("moved tile left")
        self.update2dBoard()
        self.calcLeft()