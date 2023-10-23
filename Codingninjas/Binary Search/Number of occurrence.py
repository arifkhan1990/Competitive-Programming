def firstIdx(arr, l,h, k):
    ans = -1
    while l <= h:
        m = l + (h-l) // 2
        if arr[m] == k:
            ans = m
            h = m - 1
        elif arr[m] > k:
            h = m - 1
        else:
            l = m+1
    return ans

def lastIdx(arr, l,h, k):
    ans = -1
    while l <= h:
        m = l + (h-l) // 2
        if arr[m] == k:
            ans = m
            l = m + 1
        elif arr[m] > k:
            h = m - 1
        else:
            l = m+1
    return ans 

def count(arr: [int], n: int, k: int) -> int:
    f = firstIdx(arr, 0, n-1, k)
    l = lastIdx(arr, 0, n-1, k)

    return 0 if f == -1 and l == -1 else (l-f)+1
