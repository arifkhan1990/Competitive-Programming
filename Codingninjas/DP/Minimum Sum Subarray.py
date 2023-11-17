from os import *
from sys import *
from collections import *
from math import *

def minimumSum(arr, n):
	mn = float('inf')

	sm = 0

	for i in arr:
		sm += i
		if sm > i:
			sm = i
		mn = min(mn, sm)
	return mn