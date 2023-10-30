from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def countEvenOdd(arr, n):    
    # Write your code here.
    c = Counter(arr)
    o,e = 0, 0
    for i in c:
        if c[i]%2:
            e += 1
        else:
            o += 1
    return e , o

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
