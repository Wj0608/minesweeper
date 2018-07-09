__author__ = 'DELL'

import random
import point


class Game:
    pmap = []
    map = []
    showmap = []
    temp = []
    isOver = False
    blist = []
    clicklist = []

    def __init__(self):
        # generate empty map
        while 1:
            r = int(input("Please enter the number of rows: "))
            if r > 0:
                break
            else:
                print("Input not valid.")
        while 1:
            c = int(input("Please enter the number of columns: "))
            if c > 0:
                break
            else:
                print("Input not valid.")
        for i in range(0, r):
            ll = []
            for j in range(0, c):
                ll.append(" ")
            self.showmap.append(ll)
        for i in range(0, r):
            ll = []
            for j in range(0, c):
                ll.append(0)
            self.map.append(ll)
        for i in range(0, r):
            ll = []
            for j in range(0, c):
                ll.append(0)
            self.temp.append(ll)
        for i in range(0, r):
            ll = []
            for j in range(0, c):
                ll.append(1)
            self.pmap.append(ll)
        # insert mines randomly
        while 1:
            m = int(input("Please enter the number of mines: "))
            if r*c < m:
                print("Too many mines on the board")
            else:
                break
        while m > 0:
            i = random.randint(0, r-1)
            j = random.randint(0, c-1)
            if self.map[i][j] != '*':
                self.map[i][j] = '*'
                m -= 1
                if i-1>=0 and j-1>=0:
                    if self.map[i-1][j-1] != '*':
                        self.map[i-1][j-1] += 1
                if i-1>=0:
                    if self.map[i-1][j] != '*':
                        self.map[i-1][j] += 1
                if j-1>=0:
                    if self.map[i][j-1] != '*':
                        self.map[i][j-1] += 1
                if i+1<r and j+1<c:
                    if self.map[i+1][j+1] != '*':
                        self.map[i+1][j+1] += 1
                if i+1<r:
                    if self.map[i+1][j] != '*':
                        self.map[i+1][j] += 1
                if j+1<c:
                    if self.map[i][j+1] != '*':
                        self.map[i][j+1] += 1
                if i+1<r and j-1>=0:
                    if self.map[i+1][j-1] != '*':
                        self.map[i+1][j-1] += 1
                if i-1>=0 and j+1<c:
                    if self.map[i-1][j+1] != '*':
                        self.map[i-1][j+1] += 1

    def mark(self):
        while 1:
            r = int(input("Please enter the number of rows you want to mark: ")) - 1
            if 0 <= r < len(self.map):
                break
            else:
                print("Input not valid.")
        while 1:
            c = int(input("Please enter the number of columns you want to mark: ")) - 1
            if 0 <= c < len(self.map[0]):
                break
            else:
                print("Input not valid.")
        if self.showmap[r][c] == " ":
            self.showmap[r][c] = "*"
        elif self.showmap[r][c] == "*":
            self.showmap[r][c] = " "
        else:
            print("You cannot mark that block.")

    def check(self, r, c):
        if self.showmap[r][c] == " ":
            self.blist.append(point.Point(r, c))

    def addone(self, r, c, t, m):
        if self.showmap[r][c] == " ":
            t += 1
        if self.showmap[r][c] == "*":
            m += 1
        return t, m

    def prob(self, r, c, mul):
        notMine = False
        if self.showmap[r][c] != " " and self.showmap[r][c] != '*':
            row = len(self.map)
            col = len(self.map[0])
            total = 0
            mark = 0
            if r - 1 >= 0 and c - 1 >= 0:
                total, mark = self.addone(r - 1, c - 1, total, mark)
            if r - 1 >= 0:
                total, mark = self.addone(r - 1, c, total, mark)
            if c - 1 >= 0:
                total, mark = self.addone(r, c - 1, total, mark)
            if r + 1 < row and c + 1 < col:
                total, mark = self.addone(r + 1, c + 1, total, mark)
            if r + 1 < row:
                total, mark = self.addone(r + 1, c, total, mark)
            if c + 1 < col:
                total, mark = self.addone(r, c + 1, total, mark)
            if r + 1 < row and c - 1 >= 0:
                total, mark = self.addone(r + 1, c - 1, total, mark)
            if r - 1 >= 0 and c + 1 < col:
                total, mark = self.addone(r - 1, c + 1, total, mark)
            temp = 1 - (self.showmap[r][c] - mark) / total
            if temp == 1:
                notMine = True
            mul *= temp
        return mul, notMine

    def calculate(self, p):
        r = p.x
        c = p.y
        row = len(self.map)
        col = len(self.map[0])
        multi = 1
        if r - 1 >= 0 and c - 1 >= 0:
            temp = multi
            multi, notMine = self.prob(r - 1, c - 1, multi)
            if notMine:
                return 0
        if r - 1 >= 0:
            temp = multi
            multi, notMine = self.prob(r - 1, c, multi)
            if notMine:
                return 0
        if c - 1 >= 0:
            temp = multi
            multi, notMine = self.prob(r, c - 1, multi)
            if notMine:
                return 0
        if r + 1 < row and c + 1 < col:
            temp = multi
            multi, notMine = self.prob(r + 1, c + 1, multi)
            if notMine:
                return 0
        if r + 1 < row:
            temp = multi
            multi, notMine = self.prob(r + 1, c, multi)
            if notMine:
                return 0
        if c + 1 < col:
            temp = multi
            multi, notMine = self.prob(r, c + 1, multi)
            if notMine:
                return 0
        if r + 1 < row and c - 1 >= 0:
            temp = multi
            multi, notMine = self.prob(r + 1, c - 1, multi)
            if notMine:
                return 0
        if r - 1 >= 0 and c + 1 < col:
            temp = multi
            multi, notMine = self.prob(r - 1, c + 1, multi)
            if notMine:
                return 0
        return 1 - multi

    def update(self, r, c):
        self.pmap[r][c] = 1
        row = len(self.map)
        col = len(self.map[0])
        if r-1>=0 and c-1>=0:
            self.check(r-1, c-1)
        if r-1>=0:
            self.check(r-1, c)
        if c-1>=0:
            self.check(r, c-1)
        if r+1<row and c+1<col:
            self.check(r+1, c+1)
        if r+1<row:
            self.check(r+1, c)
        if c+1<col:
            self.check(r, c+1)
        if r+1<row and c-1>=0:
            self.check(r+1, c-1)
        if r-1>=0 and c+1<col:
            self.check(r-1, c+1)

    def expand(self, r, c):
        self.temp[r][c] = 1
        self.pmap[r][c] = 1
        row = len(self.map)
        col = len(self.map[0])
        self.showmap[r][c] = self.map[r][c]
        if self.showmap[r][c] != 0:
            self.update(r, c)
        if r-1>=0 and c-1>=0:
            if self.map[r-1][c-1] != '*' and self.map[r][c] == 0:
                self.showmap[r-1][c-1] = self.map[r-1][c-1]
                self.update(r-1, c-1)
            if self.map[r-1][c-1] == 0 and self.temp[r-1][c-1] == 0:
                self.expand(r-1, c-1)
        if r-1>=0:
            if self.map[r-1][c] != '*' and self.map[r][c] == 0:
                self.showmap[r-1][c] = self.map[r-1][c]
                self.update(r-1, c)
            if self.map[r-1][c] == 0 and self.temp[r-1][c] == 0:
                self.expand(r-1, c)
        if c-1>=0:
            if self.map[r][c-1] != '*' and self.map[r][c] == 0:
                self.showmap[r][c-1] = self.map[r][c-1]
                self.update(r, c-1)
            if self.map[r][c-1] == 0 and self.temp[r][c-1] == 0:
                self.expand(r, c-1)
        if r+1<row and c+1<col:
            if self.map[r+1][c+1] != '*' and self.map[r][c] == 0:
                self.showmap[r+1][c+1] = self.map[r+1][c+1]
                self.update(r+1, c+1)
            if self.map[r+1][c+1] == 0 and self.temp[r+1][c+1] == 0:
                self.expand(r+1, c+1)
        if r+1<row:
            if self.map[r+1][c] != '*' and self.map[r][c] == 0:
                self.showmap[r+1][c] = self.map[r+1][c]
                self.update(r+1, c)
            if self.map[r+1][c] == 0 and self.temp[r+1][c] == 0:
                self.expand(r+1, c)
        if c+1<col:
            if self.map[r][c+1] != '*' and self.map[r][c] == 0:
                self.showmap[r][c+1] = self.map[r][c+1]
                self.update(r, c+1)
            if self.map[r][c+1] == 0 and self.temp[r][c+1] == 0:
                self.expand(r, c+1)
        if r+1<row and c-1>=0:
            if self.map[r+1][c-1] != '*' and self.map[r][c] == 0:
                self.showmap[r+1][c-1] = self.map[r+1][c-1]
                self.update(r+1, c-1)
            if self.map[r+1][c-1] == 0 and self.temp[r+1][c-1] == 0:
                self.expand(r+1, c-1)
        if r-1>=0 and c+1<col:
            if self.map[r-1][c+1] != '*' and self.map[r][c] == 0:
                self.showmap[r-1][c+1] = self.map[r-1][c+1]
                self.update(r-1, c+1)
            if self.map[r-1][c+1] == 0 and self.temp[r-1][c+1] == 0:
                self.expand(r-1, c+1)

    def finish(self):
        for i in range(0, len(self.showmap)):
            for j in range(0, len(self.showmap[0])):
                if self.showmap[i][j] == " " or self.showmap[i][j] == "*":
                    if self.map[i][j] != '*':
                        return False
        return True

    def display(self, m):
        for i in range(0, len(m)):
            print('', end='|')
            for j in range(0, len(m[0])):
                print(m[i][j], end='|')

            print('')
        print('')

    def click(self):
        while 1:
            r = int(input("Please enter the number of rows you want to click: ")) - 1
            if 0 <= r < len(self.map):
                break
            else:
                print("Input not valid.")
        while 1:
            c = int(input("Please enter the number of columns you want to click: ")) - 1
            if 0 <= c < len(self.map[0]):
                break
            else:
                print("Input not valid.")
        # if the block is a mine
        if self.map[r][c] == '*':
            self.showmap[r][c] = '*'
            print("Boom! You Lose.")
            self.isOver = True
        else:
            self.expand(r, c)

    def autoclick(self):
        min = 2
        tr = 0
        tc = 0
        for i in range(0, len(self.pmap)):
            for j in range(0, len(self.pmap[0])):
                if self.pmap[i][j] < min:
                    min = self.pmap[i][j]
        for i in range(0, len(self.pmap)):
            for j in range(0, len(self.pmap[0])):
                if self.pmap[i][j] == min:
                    self.clicklist.append(point.Point(i, j))
        index = random.randint(0, len(self.clicklist)-1)
        tr = self.clicklist[index].x
        tc = self.clicklist[index].y
        self.clicklist = []
        print("Click at (%d, %d)" % (tr, tc))
        if self.map[tr][tc] == '*':
            self.showmap[tr][tc] = '*'
            print("Boom! You Lose.")
            self.isOver = True
            return
        else:
            self.expand(tr, tc)
        # sort the list, then update every block in the list
        self.display(self.showmap)
        temp = []
        # delete duplicate blocks
        for i in self.blist:
            if i not in temp:
                temp.append(i)
        self.blist = temp.copy()
        # delete non-empty blocks
        i = 0
        while i < len(self.blist):
            if self.showmap[self.blist[i].x][self.blist[i].y] != " ":
                self.blist.remove(self.blist[i])
            else:
                i += 1

        for i in self.blist:
            self.pmap[i.x][i.y] = self.calculate(i)
            if self.pmap[i.x][i.y] == 1:
                self.showmap[i.x][i.y] = '*'








