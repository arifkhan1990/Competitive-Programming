from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def sortSetBitsCount(arr, size):
    stb = [[] for _ in range(31)]
    idx = 0
    for i in range(size):
        ct = 0
        for j in range(31):
            if arr[i] & (1 << j):
                ct += 1
        stb[ct].append(arr[i])
    for i in range(30, -1, -1):
        for j in range(len(stb[i])):
            arr[idx] = stb[i][j]
            idx += 1

# Taking input using fast I/0


def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    sortSetBitsCount(arr, N)
    for i in arr:
        stdout.write(str(i) + " ")
    stdout.write("\n")
    tc -= 1
