from os import *
from sys import *
from collections import *
from math import *



def minElementsToRemove(arr):
    return len(arr) - len(set(arr))
