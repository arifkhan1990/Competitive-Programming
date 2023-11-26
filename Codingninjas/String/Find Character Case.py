from os import *
from sys import *
from collections import *
from math import *

def findCase(ch):
    if ord(ch) >= 65 and ord(ch) < (65+26):
        return 1
    elif ord(ch) >= 97 and ord(ch) <= (97+26):
        return 0
    else:
        return -1