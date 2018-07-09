__author__ = 'DELL'


import game
import point


def run():
    ms = game.Game()
    ms.display(ms.showmap)
    while not ms.isOver:
        finish = False
        while not finish:
            str = input("Do you want to mark any block?(y/n): ")
            if str == "y":
                ms.mark()
                ms.display(ms.showmap)
            else:
                finish = True
        ms.click()
        ms.display(ms.showmap)
        if ms.finish():
            print("You win!")
            ms.isOver = True
    ms.display(ms.map)


def solve():
    ms = game.Game()
    ms.display(ms.map)
    while not ms.isOver:
        ms.display(ms.pmap)
        ms.autoclick()
        print("auto finish one step")
        ms.display(ms.showmap)
        if ms.finish():
            print("You win!")
            ms.isOver = True
    ms.display(ms.map)


def addone(a):
    a += 1


if __name__ == '__main__':
    # run()
    solve()




