def searchInsert(arr: [int], m: int) -> int:
    findIdx = binarySearch(arr,0,len(arr)-1, m)
    return findIdx

def binarySearch(arr, l , h, key):
    while l <= h :
        m = (l + h) // 2
        if arr[m] < key:
            l = m + 1
        elif arr[m] > key :
            h = m - 1
        else:
            return m
    return l
