from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):    
    incl, excl = 0, 0
    for i in nums:
        new_excl = max(incl, excl)
        incl = excl + i
        excl = new_excl
    return max(excl, incl)


# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1