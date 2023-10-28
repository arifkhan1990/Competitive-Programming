from os import *
from sys import *
from collections import *
from math import *

def findOdd(arr, n):
    a = Counter(arr)
    for i in set(arr):
        if a[i] % 2 == 1:
            return i
