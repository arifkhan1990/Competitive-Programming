from os import *
from sys import *
from collections import *
from math import *

def inplaceRotate(inputArray, n):
    ans = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(inputArray[i][j])
        ans.append(x)
        

    for i in range(n):
        x = inputArray[i][::-1]
        for j in range(n):
            ans[j][i] = x[j]

    return ans
