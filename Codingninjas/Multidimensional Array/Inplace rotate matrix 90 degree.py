from os import *
from sys import *
from collections import *
from math import *

def inplaceRotate(inputArray, n):
    for i in range(n):
        for j in range(i):
            inputArray[i][j], inputArray[j][i] = inputArray[j][i], inputArray[i][j]
    inputArray.reverse()
    return inputArray