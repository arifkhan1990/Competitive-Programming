def searchRange(arr: [int], x: int) -> [int]:
    f = binarySearch(arr, 0, len(arr)-1, x)

    if f == -1:
        return [-1, -1]
    else:
        s = len(arr)-1
        for i in range(f, len(arr)):
            if arr[i] != x:
                s = i - 1
                break
        return [f, s]


def binarySearch(arr, l, h, x):
    if l > h :
        return -1
    
    m = l + (h-l) // 2

    if (m == 0 and arr[m] == x) or (arr[m] == x and arr[m-1] != x ):
        return m
    
    if x <= arr[m]:
        return binarySearch(arr,l, m-1, x)
    return binarySearch(arr, m+1, h, x)