from os import *
from sys import *
from collections import *
from math import *

def sortHalfSorted(arr:list):
	hf = 0
	n = len(arr)
	tp = [0]*n

	for i in range(n-1):
		if arr[i] > arr[i+1]:
			hf = i+1
			break
	
	if hf == 0:
		return
	
	i, j, k = 0, hf, 0

	while i < hf and j < n:
		if arr[i] < arr[j]:
			tp[k] = arr[i]
			i += 1
		else:
			tp[k] = arr[j]
			j += 1
		k += 1
	
	while i < hf:
		tp[k] = arr[i]
		k += 1
		i += 1
	
	while j < n:
		tp[k] = arr[j]
		k += 1
		j += 1
	for i in range(n):
		arr[i] = tp[i]

