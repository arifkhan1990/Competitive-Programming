from os import *
from sys import *
from collections import *
from math import *

def threePointer(X:list, Y:list, Z:list):
    xl, yl,zl = len(X), len(Y), len(Z)

    i = j = k = 0
    ans = float('inf')

    while i < xl and j < yl and k < zl:
        mx = max(X[i], max(Y[j], Z[k]))
        mn = min(X[i], min(Y[j], Z[k]))

        ans = min(ans, mx -mn)

        if X[i] == mn:
            i += 1
        elif Y[j] == mn:
            j += 1
        else:
            k += 1
        
    return ans
