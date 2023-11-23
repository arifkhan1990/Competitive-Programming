from os import *
from sys import *
from collections import *
from math import *

def countStories(x, y, z):
    ans = z//y
    res = 0
    c = ans
    while c >= x:
        free = c//x
        cB = c%x
        res += free
        c = free + cB
    return ans + res