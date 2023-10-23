def minSwaps(arr):
    n = len(arr)
    ans = 0
    tp = arr.copy()
    h = {}

    tp.sort()
    for i in range(n):
        h[arr[i]] = i
    
    k = 0

    for i in range(n):
        if arr[i] != tp[i]:
            ans += 1
            k = arr[i]

            arr[i], arr[h[tp[i]]] = arr[h[tp[i]]], arr[i]
            h[k] = h[tp[i]]
            h[tp[i]] = i
    return ans