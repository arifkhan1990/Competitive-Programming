def waveFormArray(arr, n):
    arr.sort()
    for i in range(0,n, 2):

        if i < n-1 :
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
