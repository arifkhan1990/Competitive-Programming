from os import *
from sys import *
from collections import *
from math import *

def arrangeAuthors(s):
    ans = []
    k = 1
    for i in s:
        ans.append(str(k)+". "+i[0])
        k += 1
        c = 65
        for j in range(1, len(i)):
            ans.append(chr(c)+ ". " + i[j])
            c += 1
    return ans
