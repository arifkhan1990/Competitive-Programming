from os import *
from sys import *
from collections import *
from math import *

def xorQuery(queries):
    ans = []
    for i in queries:
        if i[0] == 1:
            ans.append(i[1])
        else:
            for j in range(len(ans)):
                ans[j] ^= i[1] 
    return ans