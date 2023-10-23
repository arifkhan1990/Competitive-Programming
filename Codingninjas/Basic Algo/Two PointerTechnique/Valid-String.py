from os import *
from sys import *
from collections import *
from math import *

def checkValidString(s):
    l , h = 0, 0
    for i in s:
        l += 1 if i == '(' else -1
        h += 1 if i != ')' else -1
        if h < 0:
            break
        l = max(l, 0)
    return 1 if l == 0 else 0