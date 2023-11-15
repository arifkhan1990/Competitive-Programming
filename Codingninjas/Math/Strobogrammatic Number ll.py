

def number(n, l):
    if n == 0: return [""]
    if n == 1: return ["1", "0", "8"]

    mid = number(n-2, l)

    res = []

    for m in mid:
        if n != l:
            res.append("0" + m + "0")
        res.append("8" + m + "8")
        res.append("1" + m + "1")
        res.append("9" + m + "6")
        res.append("6" + m + "9")
    return res

def findStrobogrammatic(n):
    ans = number(n, n)
    return ans