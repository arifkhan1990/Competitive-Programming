from os import *
from sys import *
from collections import *
from math import *

def switchingSubarray(A, N): 
    if N == 1:
        return 1
    mxl , cnt = 1, 1
    for i in range(1, N):
        if (i&1 == 0 and A[i] == A[i-2]) or (i&1 == 1 and A[i] == A[i-2]):
            cnt += 1
        else:
            cnt = 2
        mxl = max(mxl, cnt)
    return mxl
            
  