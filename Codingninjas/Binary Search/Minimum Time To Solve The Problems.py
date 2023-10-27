def isValid(arr, m, k):
    i, s = 1, 0
    for j in arr:
        if s + j <= m:
            s += j
        else:
            i += 1
            s = j
        if i > k or j > m:
            return 0
    return 1

def minimumRequiredTime(subjects, k):
    l, h = 0, sum(subjects)

    ans = -1
    while l <= h:
        m = l + (h-l)//2
        if isValid(subjects, m , k):
            ans = m
            h = m - 1
        else:
            l = m + 1
    return ans

