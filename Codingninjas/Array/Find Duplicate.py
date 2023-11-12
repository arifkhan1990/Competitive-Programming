
import sys

def duplicateNumber(arr, n) :
    sm = ((n-1)*(n-2)) // 2
    ar_sm = sum(arr)

    return ar_sm - sm