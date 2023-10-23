from os import *
from sys import *
from collections import *
from math import *

def findRowK(mat):
    ans = -1
    for i in range(len(mat)):
        if sum(mat[i]) - mat[i][i] == -1 or sum(mat[i]) - mat[i][i] == 0:
            for j in range(len(mat[0])):
                if mat[i][j] != 1:
                    ans = -1
            ans = i
    return ans

