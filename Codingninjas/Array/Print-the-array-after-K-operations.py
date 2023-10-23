from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout

def newArr(arr, n, x):
    for i in range(n):
        arr[i] = abs(x-arr[i])
    return arr
    
def printArrayAfterKOperations(arr, N, K):

    if K == 0:
        return arr
    if K%2 == 0:
        K = 2
    else:
        K = 1
    for i in range(K):
        arr = newArr(arr, N, max(arr))
    return arr


# Taking input using fast I/0.
def takeInput():
    N, K = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, K, arr


tc = int(input())
while tc > 0:
    N, K, arr = takeInput()
    sol = printArrayAfterKOperations(arr, N, K)
    for i in sol:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    tc -= 1
