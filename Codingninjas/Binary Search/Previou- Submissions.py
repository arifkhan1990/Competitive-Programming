def search(arr, n, k):
    l , h = 0, n-1
    while l <= h:
 
        m = (l + h )//2

        if arr[m] == k:
            return m
        
        if arr[l] <= arr[m]:
            if k < arr[m] and  arr[l] <= k:
                h = m-1
            else:
                l = m + 1
        else:
            if k >= arr[m] and  arr[h] >= k:
                l = m + 1
            else:
                h = m - 1

    return -1