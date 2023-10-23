from os import *
from sys import *
from collections import *
from math import *

def rowWaveForm(mat):
    ans = []

    for i in range(len(mat)):
        if i%2 == 0:
            ans.extend(mat[i])
        else:
            ans.extend(mat[i][::-1])
    return ans