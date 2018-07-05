__author__ = 'DELL'

import time
import os

def Map(r,c):
    l = []
    for i in range(0, int(r)):
        ll = []
        for j in range(0, int(c)):
            ll.append(0)
        l.append(ll)
    return l

def run():

    row = input("Please enter the number of rows: ")
    col = input("Please enter the number of columns: ")
    map = Map(row,col)
    print(map)


if __name__ == '__main__':
    run()
