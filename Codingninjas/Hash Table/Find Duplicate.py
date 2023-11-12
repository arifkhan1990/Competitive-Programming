import sys

def duplicateNumber(arr, n) :
    ans = {}
    for i in arr:
        if i not in  ans:
            ans[i] = 1
        else:
            ans[i] += 1
    
    for i in list(set(arr)):
        if ans[i] > 1:
            return i