from os import *
from sys import *
from collections import *
from math import *

def search(matrix, x):

    # O(n) solution
    n = len(matrix)
    if n == 0:
        return -1, -1
    i, j = 0, n-1

    while i < n and j > 0:
        if matrix[i][j] == x:
            return i, j
        elif matrix[i][j] > x:
            j -= 1
        else:
            i += 1
    return -1, -1

    # O(n^2) solution
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         if matrix[i][j] == x:
    #             return [i,j]
    # return [-1, -1]