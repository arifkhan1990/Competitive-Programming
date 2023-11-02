from os import *
from sys import *
from collections import *
from math import *


def smallestWindow(s, x):
    l1,l2 = len(s), len(x)
    if l1 < l2 :
        return ""
    
    hp = [0]*256
    hs = [0]*256

    for i in range(0,l2):
        hp[ord(x[i])] += 1
    
    start, start_idx, mn_l = 0,-1,float('inf')
    cnt = 0
    for j in range(0,l1):
        hs[ord(s[j])] += 1

        if hs[ord(s[j])] <= hp[ord(s[j])]:
            cnt += 1
        
        if cnt == l2:
            while hs[ord(s[start])] > hp[ord(s[start])] or hp[ord(s[start])] == 0:
                if hs[ord(s[start])] > hp[ord(s[start])]:
                    hs[ord(s[start])] -= 1
                start += 1

            lw = j - start + 1
            if mn_l > lw:
                mn_l = lw
                start_idx = start
    if start_idx == -1:
        return ""
    return s[start_idx:start_idx+mn_l]