from os import *
from sys import *
from collections import *
from math import *

def isMatrixSymmetric(matrix):
    for i in range(len(matrix)):
        r = matrix[i]
        c = []
        for j in range(len(matrix[i])):
            c.append(matrix[j][i])
        if r != c:
            return 0
    return 1