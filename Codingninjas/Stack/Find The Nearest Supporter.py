from os import *
from sys import *
from collections import *
from math import *

def prevSmall(arr, n):
    s = []
    ans = []
    
    for i in range(n):
        cur_rating = arr[i]

        while s and s[-1] >= cur_rating:
            s.pop()
        
        if not s:
            ans.append(-1)
        else:
            ans.append(s[-1])
        
        s.append(cur_rating)
    return ans
