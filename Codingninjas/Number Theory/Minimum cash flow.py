from os import *
from sys import *
from collections import *
from math import *

def minCashFlow(money, n):
    ans = [0]*n
    res = 0
    for i in range(n):
        for j in range(n):
            ans[i] -= money[i][j]
            ans[j] += money[i][j]
    
    for x in ans:
        if x < 0:
            res += abs(x)
    return res