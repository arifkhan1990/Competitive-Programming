

def countPositiveNegativePairs(arr, n):
    mp = {}
    ans = 0
    for i in arr:
        if i < 0:
            mp[i] = mp.get(i, 0) + 1
    
    for i in arr:
        if -i in mp:
            ans += mp.get(-i)
    return ans