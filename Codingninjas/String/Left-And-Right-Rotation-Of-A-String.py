from os import *
from sys import *
from collections import *
from math import *

def leftRotate(strr, d):    
    if d <= len(strr):
        return strr[d:] + strr[:d]
    else:
        return leftRotate(strr, d%len(strr))
    
def rightRotate(strr, d):   
    if d <= len(strr):
        return  strr[len(strr)-d: ] + strr[:len(strr)-d]
    else:
        return rightRotate(strr, d%len(strr))
