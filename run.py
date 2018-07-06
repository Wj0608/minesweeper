__author__ = 'DELL'

import time
import os
import game


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


if __name__ == '__main__':
    run()
