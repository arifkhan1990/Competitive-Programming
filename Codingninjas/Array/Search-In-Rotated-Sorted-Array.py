def search(arr, target) :
    l = 0
    h = len(arr) - 1

    return findResult(arr,l,h,target)

def findResult(arr,l,h,target):
    if l > h:
        return -1
    
    m = (l+h)//2
    if arr[m] == target:
        return m

    if arr[l] <= arr[m]:
        if target >= arr[l] and target <= arr[m]:
            return findResult(arr, l, m-1, target)
        return findResult(arr, m+1, h, target)
    
    if target >= arr[m] and target <= arr[h]:
        return findResult(arr, m+1, h, target)
    return findResult(arr, l, m-1, target)
