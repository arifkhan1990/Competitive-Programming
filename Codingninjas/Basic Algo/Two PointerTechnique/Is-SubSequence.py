from os import *
from sys import *
from collections import *
from math import *

def isSubSequence(str1, str2):
    l, r = 0, 0
    ans = ""
    while l < len(str1) and r < len(str2):
        if str1[l] == str2[r]:
            ans += str1[l]
            l , r = l+1, r+1
        else:
            r += 1
    return True if str1 == ans else False
