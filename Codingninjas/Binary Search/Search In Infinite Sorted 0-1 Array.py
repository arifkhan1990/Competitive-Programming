import sys
def firstOne(get):
    s, e = 0, sys.maxsize+1
    while s <= e:
        m = s + (e-s)//2
        if get(m):
            e = m - 1
        else:
            s = m + 1
    return s