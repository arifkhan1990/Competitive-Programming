from os import *
from sys import *
from collections import *
from math import *

import sys
from sys import stdin

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def rotateMatRight(mat, n, m, k):
	ans = []
	res = []
	
	k = k%m
	l = m - k

	for i in range(l,m):
		x = []
		for j in range(n):
			x.append(mat[j][i])
		ans.append(x)
	
	for i in range(l):
		x = []
		for j in range(n):
			x.append(mat[j][i])
		ans.append(x)

	for i in range(n):
		for j in range(m):
			res.append(ans[j][i])
	return res


# Taking the input.
def takeInput() :
	n, m, k = map(int, sys.stdin.readline().strip().split(" "))
	mat = [list(map(int, sys.stdin.readline().strip().split(" "))) for row in range(n)]
	return n, m, k, mat

# Printing the Matrix.
def printAns(ans):
	for i in ans:
		print(i, end = ' ')
	print('')

# Main.
t = int(input().strip())
for i in range(t):
	n, m, k, mat = takeInput()
	ans = rotateMatRight(mat, n, m, k)
	printAns(ans)