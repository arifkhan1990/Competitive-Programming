from math import *
from collections import *
from sys import *
from os import *

from functools import lru_cache

@lru_cache()
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input())
print(fib(n))