from os import *
from sys import *
from collections import *
from math import *


def square(l,h,a):
    ans = 0
    while l <= h:
        m = l + (h - l) // 2
        sq = m*m
        if sq == a:
            ans = m
            return m
        elif sq > a:
            h = m-1
        else:
            ans = max(ans, m)
            l = m+1
    return ans 
def squareRoot(a):
    return square(0,a,a)
