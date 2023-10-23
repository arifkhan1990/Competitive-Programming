from os import *
from sys import *
from collections import *
from math import *
from functools import lru_cache

@lru_cache()
def fibonacciNumber(n):
    d = 1000000007
    if n==1 or n==2:
        return 1
    return (fibonacciNumber(n-1)%d+fibonacciNumber(n-2)%d)%d
