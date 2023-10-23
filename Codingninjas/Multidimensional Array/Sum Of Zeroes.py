from os import *
from sys import *
from collections import *
from math import *

def coverageOfMatrix(mat):
    ans = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                for k in range(4):
                    r = i+dr[k]
                    c = j+dc[k]

                    if r >= 0 and r < len(mat) and c >= 0 and c < len(mat[i]) and mat[r][c] == 1:
                        ans += 1
    return ans