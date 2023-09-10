from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    ans = 0
    currSum = 0
    for i in range(n):
        currSum = currSum + arr[i]
        ans = max(ans, currSum)

        if currSum < 0:
            currSum = 0

    return ans

#taking inpit using fast I/O
def takeInput() :

    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))