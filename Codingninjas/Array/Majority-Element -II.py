from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	cnt = Counter(arr)
	ans = []
	for i in set(arr):
		if cnt[i] > floor(len(arr)/3):
			ans.append(i)
	return ans