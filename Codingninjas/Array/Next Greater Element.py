from os import *
from sys import *
from collections import *
from math import *

def nextGreaterElement(arr, n):
	# O(n^2) time
	# ans = []
	# for i in range(n-1):
	# 	x = -1
	# 	for j in range(i+1,n):
	# 		if arr[i] < arr[j]:
	# 			x = arr[j]
	# 			break
	# 	ans.append(x)
	# ans.append(-1)
	# return ans
	ans = []
	for i in range(n):
		while ans and ans[-1].get("v") < arr[i]:
			d = ans.pop()
			arr[d.get("idx")] = arr[i]
		ans.append({"v": arr[i], "idx": i})
	
	while ans:
		d = ans.pop()
		arr[d.get("idx")] = -1
	return arr