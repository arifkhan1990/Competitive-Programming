from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit



def findTriplets(arr, n):
    ans = []
    arr.sort()

    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        l,r = i + 1, n - 1
        while l < r:
            if (arr[i] + arr[l] + arr[r]) < 0:
                l += 1
            elif (arr[i] + arr[l] + arr[r]) > 0:
                r -= 1
            else:
                ans.append([arr[i],arr[l],arr[r]])
                l, r = l+1, r - 1
    return ans



# Taking input using fast I/0
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = findTriplets(arr, N)
    if len(ans) == 0:
        stdout.write("-1\n")
    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
