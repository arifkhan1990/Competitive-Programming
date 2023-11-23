from os import *
from sys import *
from collections import *
from math import *

def convertString(str):
    ans =""
    for i in range(len(str)):
        if i == 0 or str[i-1] == ' ':
            ans += str[i].upper()
        else:
            ans += str[i]
    
    return ans