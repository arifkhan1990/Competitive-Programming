from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    #   Write your code here
    s = ""
    for i in arr:
        s += str(i)
    ans = []
    sN = str(int(s) + 1)
    for i in sN:
        ans.append(int(i))
    return ans
