from os import *
from sys import *
from collections import *
from math import *

def findGoodMatrix(arr): 
    r = set()
    c = set()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                r.add(i)
                c.add(j)
    for i in range(len(r)):

        for j in range(len(arr[0])):
            arr[r[i]][j] = 0

        for j in range(len(arr)):
            arr[j][c[i]] = 0
    
    return arr