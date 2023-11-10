from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def countEvenOdd(arr, n):    
    a = Counter(arr)
    od,ev = 0, 0
    for i in set(arr):
        if a[i]%2 == 0:
            ev += 1
        else:
            od += 1
    return od, ev

# Print answer.
def printAns(ans):

    print(ans[0], end=" ")
    print(ans[1])

# Taking inpit using fast I/O.
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n

# Main.
t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    ans = countEvenOdd(arr,n)
    printAns(ans)