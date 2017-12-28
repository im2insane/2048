class Helper:
    def __init__(self):
        pass

    def swap(self,x,y,lst):
        temp = lst[x]
        lst[x] = lst[y]
        lst[y] = temp

        return lst

    def swap2d(self,r1,c1,r2,c2,lst):
        temp = lst[r1][c1]
        lst[r1][c1] = lst[r2][c2]
        lst[r2][c2] = temp

        return lst

    def printLst(self,lst):
        for i in range(0, len(lst)):
            if i % 4 == 0:
                print()
            print(lst[i], end=" ")
        print()

    def print2DLst(self,lst):
        for i in range(0,len(lst)):
            print(*lst[i])