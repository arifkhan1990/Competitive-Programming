from os import *
from sys import *
from collections import *
from math import *

def lengthOfLongestSubstring(s):
	ans = 0
	ch = [0]*128

	l = r = 0
     
	while r < len(s):
		x = s[r]
		ch[ord(x)] += 1

		while ch[ord(x)] > 1:
			y = s[l]
			ch[ord(y)] -= 1
			l += 1
		ans = max(ans, r-l+1)
	
		r += 1
	return ans
    