from os import *
from sys import *
from collections import *
from math import *

def rotate(arr, n):
    # Write your code here.
    i, j = 0 , n-1
    while i != j:
        arr[i],arr[j] = arr[j], arr[i]
        i += 1
    