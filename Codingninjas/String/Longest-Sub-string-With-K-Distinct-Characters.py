from os import *
from sys import *
from collections import *
from math import *

def getLengthofLongestSubstring(s, k):
    ans = 0
    for i in range(len(s)):
        subStr = ""
        for j in range(i, len(s)):
            subStr += s[j]
            if len(set(subStr)) <= k:
                ans = max(ans, len(subStr))
                # print(subStr, len(set(subStr)))
    return ans