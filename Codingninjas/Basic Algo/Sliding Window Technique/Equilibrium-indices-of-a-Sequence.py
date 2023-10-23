from os import *
from sys import *
from collections import *
from math import *

import sys

def findEquilibriumIndices(s1):
    # Write your code here.
    s = sum(s1)
    i , j = 0, 0
    ans = []
    while i < len(s1):
        s -= s1[i]
        if s == j:
            ans.append(i)
        j += s1[i]
        i += 1
    return ans


# Taking input using fast I/O
def takeInput():
    n = int(input())
    sequence = list(map(int, input().strip().split(" ")))
    return sequence, n

# Main
t = int(input())
while t:
    sequence, n = takeInput()
    print(*findEquilibriumIndices(sequence))
    t = t-1