from os import *
from sys import *
from collections import *
from math import *

def findTriplet(arr,n):
	arr.sort()

	for i in range(n-1, -1, -1):
		t = arr[i]
		j = 0
		k = i-1
		while j < k:
			if arr[j] + arr[k] == t:
				return [t, arr[j], arr[k]]
			elif arr[j] + arr[k] < t:
				j += 1
			else:
				k -= 1
	return []