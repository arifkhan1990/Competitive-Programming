def isValid(arr, x, k):
    c , lp = 1, arr[0]

    for i in arr:
        if i - lp >= x:
            c += 1
            if c == k:
                return 1
            lp = i
    return 0
def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    s, e, ans = 0, stalls[-1], -1

    while s <= e:
        m = s + (e-s) // 2
        if isValid(stalls, m, k):
            ans = m
            s = m + 1
        else:
            e = m - 1
    return ans