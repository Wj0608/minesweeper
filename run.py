__author__ = 'DELL'

import time
import os
import game

def Map(r,c):
    l = []
    for i in range(0, int(r)):
        ll = []
        for j in range(0, int(c)):
            ll.append(0)
        l.append(ll)
    return l

def run():
    ms = game.Game()
    ms.display(ms.map)
    while not ms.isOver:
        ms.click()
        ms.display(ms.showmap)
        if ms.finish():
            print("You win!")
            ms.isOver = True
    ms.display(ms.map)


if __name__ == '__main__':
    run()
