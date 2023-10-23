def findPeakElement(arr: [int]) -> int:
    l,h = 0, len(arr)-1
    while l <= h:
        m = l + (h-l)//2
        if m>=0 and m < len(arr):
            if m == 0 and arr[m] > arr[m+1]:
                return m
            elif m == len(arr)-1 and arr[m] > arr[m-1]:
                return m
        if arr[m] > arr[m-1] and  arr[m] > arr[m+1]:
            return m
        elif arr[m] < arr[l]:
            h = m-1
        else:
            l = m+1
    return 0