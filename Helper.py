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
        print()

    def print2DLst(self,lst):
        for i in range(0,len(lst)):
            print(*lst[i])
        print()

    def boardTo2D(self,lst):
        newLst = []
        for i in range(0,len(lst),4):
            temp = lst[i:i+4]
            newLst.append(temp)
        return newLst

    def tileUp(self,lst):
        for i in range(0, len(lst)):
            if lst[i] == 0:
                pos = i
                while (pos <= len(lst) - 1):
                    if lst[pos] != 0:
                        lst = self.swap(i, pos, lst)
                        break
                    else:
                        pos += 4
        return lst

    def tileDown(self,lst):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == 0:
                pos = i
                while (pos >= 0):
                    if lst[pos] != 0:
                        lst = self.swap(i, pos, lst)
                        break
                    else:
                        pos -= 4
        return lst

    def tileRight(self,lst):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == 0:
                pos = i
                iterations = pos % 4
                while iterations != -1:
                    if lst[pos] != 0:
                        lst = self.swap(pos, i, lst)
                        break
                    else:
                        pos -= 1
                        iterations -= 1

        return lst