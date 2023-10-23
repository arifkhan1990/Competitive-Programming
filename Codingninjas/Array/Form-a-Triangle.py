from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def possibleToMakeTriangle(arr):
    arr.sort()

    for i in range(len(arr) - 2):
        if triangleSideSum(arr[i],arr[i+1],arr[i+2]) and triangleSideSum(arr[i+1],arr[i+2],arr[i]) and triangleSideSum(arr[i],arr[i+2],arr[i+1]):
            return True
    return False

def triangleSideSum(x,y,z):
    if x+y > z:
        return True
    return False
# Main code.
t = int(input().strip())

for i in range(t):
    n = list(map(int, stdin.readline().strip().split(" ")))

    if len(n) > 1:
        arr = n
    else:
        arr = list(map(int, stdin.readline().strip().split(" ")))

    if (possibleToMakeTriangle(arr)):
        print("YES")
    else:
        print("NO")
